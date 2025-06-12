# app/utils/logger.py
import logging
import asyncio
import queue
import threading
from typing import Optional
from app.services.storage import StorageService

class DatabaseHandler(logging.Handler):
    def __init__(self, storage_service: StorageService):
        super().__init__()
        self.storage = storage_service
        self.log_queue = queue.Queue()
        self.worker_thread: Optional[threading.Thread] = None
        self.shutdown_event = threading.Event()
        self.start_worker()
    
    def emit(self, record):
        """Add log record to queue (thread-safe)"""
        try:
            # Extract component from the logger name
            parts = record.name.split('.')
            component = parts[-1].upper() if len(parts) > 0 else "SYSTEM"
            
            # Prepare metadata
            metadata = {
                "module": getattr(record, 'module', 'unknown'),
                "function": record.funcName,
                "line": record.lineno
            }
            
            # Put log data in queue instead of creating asyncio task
            log_data = {
                'level': record.levelname,
                'component': component,
                'message': self.format(record),
                'metadata': metadata
            }
            
            self.log_queue.put_nowait(log_data)
            
        except queue.Full:
            # Queue is full, handle error
            self.handleError(record)
        except Exception:
            self.handleError(record)
    
    def start_worker(self):
        """Start background worker thread to process logs"""
        self.worker_thread = threading.Thread(
            target=self._worker_loop,
            daemon=True,
            name="log_storage_worker"
        )
        self.worker_thread.start()
    
    def _worker_loop(self):
        """Worker thread that processes queued logs with its own event loop"""
        # Create a new event loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            while not self.shutdown_event.is_set():
                try:
                    # Get log record with timeout to allow periodic shutdown checks
                    log_data = self.log_queue.get(timeout=1.0)
                    
                    # Store log asynchronously in this thread's event loop
                    loop.run_until_complete(
                        self.storage.store_log(
                            log_data['level'],
                            log_data['component'],
                            log_data['message'],
                            log_data['metadata']
                        )
                    )
                    
                    self.log_queue.task_done()
                    
                except queue.Empty:
                    # Timeout occurred, continue loop to check shutdown
                    continue
                except Exception as e:
                    # Log storage failed, but don't crash the worker
                    print(f"Error storing log: {e}")
                    
        except Exception as e:
            print(f"Critical error in log worker thread: {e}")
        finally:
            # Clean up remaining queue items
            while not self.log_queue.empty():
                try:
                    self.log_queue.get_nowait()
                    self.log_queue.task_done()
                except queue.Empty:
                    break
            
            loop.close()
    
    def close(self):
        """Shutdown the handler gracefully"""
        self.shutdown_event.set()
        
        # Wait for worker thread to finish
        if self.worker_thread and self.worker_thread.is_alive():
            self.worker_thread.join(timeout=5.0)
            
        super().close()

def setup_logging(storage_service: StorageService):
    root_logger = logging.getLogger()
    
    # Clear existing handlers to avoid duplicates
    root_logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
    ))
    root_logger.addHandler(console_handler)
    
    # Database handler with queue-based processing
    db_handler = DatabaseHandler(storage_service)
    db_handler.setFormatter(logging.Formatter('%(message)s'))
    root_logger.addHandler(db_handler)
    
    # Set level
    root_logger.setLevel(logging.INFO)
    
    return db_handler  # Return handler for cleanup in shutdown

# Optional: Enhanced setup with cleanup registration
def setup_logging_with_cleanup(storage_service: StorageService):
    """Setup logging with automatic cleanup registration"""
    import atexit
    
    db_handler = setup_logging(storage_service)
    
    # Register cleanup function to run on program exit
    atexit.register(db_handler.close)
    
    return db_handler

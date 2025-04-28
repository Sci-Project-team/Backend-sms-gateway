# app/utils/logger.py
import logging
from app.services.storage import StorageService

class DatabaseHandler(logging.Handler):
    def __init__(self, storage_service: StorageService):
        super().__init__()
        self.storage = storage_service
    
    def emit(self, record):
        try:
            # Extract component from the logger name
            parts = record.name.split('.')
            component = parts[-1].upper() if len(parts) > 0 else "SYSTEM"
            
            # Prepare metadata
            metadata = {
                "module": record.module,
                "function": record.funcName,
                "line": record.lineno
            }
            
            # Store log asynchronously
            import asyncio
            asyncio.create_task(
                self.storage.store_log(
                    record.levelname,
                    component,
                    self.format(record),
                    metadata
                )
            )
        except Exception:
            self.handleError(record)

def setup_logging(storage_service: StorageService):
    root_logger = logging.getLogger()
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
    ))
    root_logger.addHandler(console_handler)
    
    # Database handler
    db_handler = DatabaseHandler(storage_service)
    db_handler.setFormatter(logging.Formatter('%(message)s'))
    root_logger.addHandler(db_handler)
    
    # Set level
    root_logger.setLevel(logging.INFO)
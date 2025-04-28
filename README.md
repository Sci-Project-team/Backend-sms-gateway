# SMS Gateway API

A REST API for sending and receiving SMS messages through a GSM module, built with FastAPI.

## Features

- User authentication with JWT tokens
- Send SMS messages
- Receive SMS messages
- Check inbox
- View logs
- Admin panel for user management

## Quick Start

### Prerequisites

- Python 3.8+
- pip
- SQLite (included)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Sci-Project-team/Backend-sms-gateway.git
   cd sms-gateway-api
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your settings:
   ```
   API_KEY=your_api_key_here
   SECRET_KEY=your_secret_key_here
   SIMULATION_MODE=True  # Set to False when using real GSM hardware
   use this 
   SIMULATION_MODE=True
   GSM_PORT=COM3 
   GSM_BAUDRATE=9600
   API_KEY=test_api_key

   ```


### Running the API

```
uvicorn app.main:app --reload
or
 python -m app.main
```

The API will be available at http://localhost:8000

## API Documentation

- Interactive API documentation: http://localhost:8000/docs
- ReDoc API documentation: http://localhost:8000/redoc

## API Endpoints

### Authentication

- `POST /auth/register` - Create a new user account
- `POST /auth/login` - Get an access token

### SMS Operations

- `POST /sms` - Send an SMS message
- `GET /sms/inbox` - View received messages
- `GET /logs` - View system logs

### Admin (requires API key)

- `GET /admin/users` - List all users
- `GET /admin/messages` - List all messages

### Development Only

- `POST /sms/simulate-receive` - Simulate receiving an SMS message
  - Query parameters:
    - `phone_number`: Sender's phone number
    - `message`: Message content


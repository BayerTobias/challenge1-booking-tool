# API Documentation for Appointment Management

This API facilitates the management of appointments between doctors and patients.

## Endpoints

### 1. Authentication

**POST /api/token/**

- **Description**: Obtain a token for authentication.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

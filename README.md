# API Documentation for Appointment Management

This API facilitates the management of appointments between doctors and patients.

## Endpoints

### 1. Authentication

**POST /auth/login/**

- **Description**: Obtain a token for authentication.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 2. Doctors

**GET /api/Doctors/**

- **Description**: Retrieve a list of all doctors.
- **Response Example**:

```json
[
  {
    "id": 1,
    "user": {
      "username": "doctor1",
      "id": 1
    },
    "title": "Dr.",
    "speciality": "Radiologist",
    "name": "Dr. Smith"
  },
  {
    "id": 2,
    "user": {
      "username": "doctor2",
      "id": 2
    },
    "title": "Prof. Dr.",
    "speciality": "General Medicine",
    "name": "Prof. Dr. Müller"
  }
]
```

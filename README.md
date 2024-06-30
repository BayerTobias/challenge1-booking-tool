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

**GET /api/doctors/**

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
      "title": "dr",
      "speciality": "radiologe",
      "name": "Jon Smith"
    },
    {
      "id": 2,
      "user": {
        "username": "doctor2",
        "id": 2
      },
      "title": "prof_dr.",
      "speciality": "allgemeinmedizin",
      "name": "Barbra Müller"
    }
  ]
  ```

**POST /api/doctors/**

- **Description**: Create a new doctor.
- **Request Body**:

  ```json
  {
    "user": {
      "username": "doctor_new",
      "password": "password123"
    },
    "title": "dr",
    "speciality": "hautarzt",
    "name": "Joe Brown"
  }
  ```

- **Response Example**:
  ```json
  {
    "id": 3,
    "user": {
      "username": "doctor_new",
      "id": 3
    },
    "title": "dr",
    "speciality": "hautarzt",
    "name": "Joe Brown"
  }
  ```

**DELETE /api/doctors/{doctor_id}/**

- **Description**: Delete a specific doctor by ID.
- **Response Example**:
  ```json
  {
    "message": "Deleted successfully"
  }
  ```

### 3. Patients

**GET /api/patients/**

- **Description**: Retrieve a list of all patients.
- **Response Example**:

  ```json
  [
    {
      "id": 1,
      "user": {
        "username": "patient1",
        "id": 4
      },
      "name": "John Doe"
    },
    {
      "id": 2,
      "user": {
        "username": "patient2",
        "id": 5
      },
      "name": "Jane Smith"
    }
  ]
  ```

**POST /api/patients/**

- **Description**: Create a new patient.
- **Request Body**:

  ```json
  {
    "user": {
      "username": "patient_new",
      "password": "password456"
    },
    "name": "Michael Johnson"
  }
  ```

- **Response Example**:
  ```json
  {
    "id": 3,
    "user": {
      "username": "patient_new",
      "id": 6
    },
    "name": "Michael Johnson"
  }
  ```

**DELETE /api/patients/{patient_id}/**

- **Description**: Delete a specific patient by ID.
- **Response Example**:
  ```json
  {
    "message": "Deleted successfully"
  }
  ```

### 3. Appointments

**GET /api/appointments/**

- **Description**: Retrieve a list of all appointments involving the current user (either as a doctor or patient).
- **Response Example**:

  ```json
  [
    {
      "id": 1,
      "title": "Check-up",
      "description": "Regular health check-up",
      "doctor": 1,
      "patient": 1,
      "appointment_date": "2024-07-01"
    },
    {
      "id": 2,
      "title": "Dental Cleaning",
      "description": "Routine dental cleaning appointment",
      "doctor": 1,
      "patient": 2,
      "appointment_date": "2024-07-05"
    }
  ]
  ```

**POST /api/appointments/**

- **Description**: Create a new appointment between a doctor and a patient.
- **Request Body**:

  ```json
  {
    "title": "Physical Examination",
    "description": "Comprehensive physical examination",
    "doctor": 1,
    "patient": 2,
    "appointment_date": "2024-07-10"
  }
  ```

- **Response Example**:
  ```json
  {
    "id": 5,
    "title": "Physical Examination",
    "description": "Comprehensive physical examination",
    "created_at": "2024-06-30",
    "appointment_date": "2024-07-10",
    "doctor": 1,
    "patient": 5
  }
  ```

**DELETE /api/appointments/{appointment_id}/**

- **Description**: Delete a specific appointment by ID.
- **Response Example**:
  ```json
  {
    "message": "Deleted successfully"
  }
  ```

## Notes

- **Doctor Account**: Username: doctor1 Password: Testpasswort
- **Patient Account**: Username: patient1 Password: Testpasswort

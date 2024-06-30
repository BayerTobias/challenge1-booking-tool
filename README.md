API Documentation for Appointment Management
This API allows for the management of appointments between doctors and patients.

Endpoints

1. Authentication
   POST /api/token/

Description: Obtain a JWT token for authentication.
Request Body:
{
"username": "string",
"password": "string"
}
Response:
{
"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
} 2. Doctors
GET /api/doctors/

Description: Retrieve a list of all doctors.
Response Example:
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
POST /api/doctors/

Description: Create a new doctor.
Request Body:
{
"user": {
"username": "doctor_new",
"password": "password123"
},
"title": "Dr.",
"speciality": "Dermatologist",
"name": "Dr. Brown"
}
Response Example:
{
"id": 3,
"user": {
"username": "doctor_new",
"id": 3
},
"title": "Dr.",
"speciality": "Dermatologist",
"name": "Dr. Brown"
}
DELETE /api/doctors/{doctor_id}/

Description: Delete a specific doctor by ID.
Response Example:
{
"message": "Deleted successfully"
} 3. Patients
GET /api/patients/

Description: Retrieve a list of all patients.
Response Example:
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
POST /api/patients/

Description: Create a new patient.
Request Body:
{
"user": {
"username": "patient_new",
"password": "password456"
},
"name": "Michael Johnson"
}
Response Example:
{
"id": 3,
"user": {
"username": "patient_new",
"id": 6
},
"name": "Michael Johnson"
}
DELETE /api/patients/{patient_id}/

Description: Delete a specific patient by ID.
Response Example:
{
"message": "Deleted successfully"
} 4. Appointments
GET /api/appointments/

Description: Retrieve a list of all appointments involving the current user (either as a doctor or patient).
Response Example:
[
{
"id": 1,
"doctor": {
"id": 1,
"user": {
"username": "doctor1",
"id": 1
},
"title": "Dr.",
"speciality": "Radiologist",
"name": "Dr. Smith"
},
"patient": {
"id": 1,
"user": {
"username": "patient1",
"id": 4
},
"name": "John Doe"
},
"date": "2024-07-01"
},
{
"id": 2,
"doctor": {
"id": 2,
"user": {
"username": "doctor2",
"id": 2
},
"title": "Prof. Dr.",
"speciality": "General Medicine",
"name": "Prof. Dr. Müller"
},
"patient": {
"id": 2,
"user": {
"username": "patient2",
"id": 5
},
"name": "Jane Smith"
},
"date": "2024-07-05"
}
]
POST /api/appointments/

Description: Create a new appointment between a doctor and a patient.
Request Body:
{
"doctor": 1,
"patient": 2,
"date": "2024-07-10"
}
Response Example:
{
"id": 3,
"doctor": {
"id": 1,
"user": {
"username": "doctor1",
"id": 1
},
"title": "Dr.",
"speciality": "Radiologist",
"name": "Dr. Smith"
},
"patient": {
"id": 2,
"user": {
"username": "patient2",
"id": 5
},
"name": "Jane Smith"
},
"date": "2024-07-10"
}
DELETE /api/appointments/{appointment_id}/

Description: Delete a specific appointment by ID.
Response Example:
{
"message": "Deleted successfully"
}

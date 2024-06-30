from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer


class LoginView(ObtainAuthToken):

    def post(self, request):
        """
        Handle POST request to authenticate user and provide a token.

        Args:
            request: HTTP request object containing user credentials.

        Returns:
            Response: JSON response containing the authentication token if login is successful.
                      Returns HTTP 200 status.
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_200_OK)


class PatientView(APIView):

    def get(self, request, patient_id=None):
        """
        Handle GET request to retrieve patient information.

        Args:
            request: HTTP request object.
            patient_id: Optional ID of the patient to retrieve. If not provided, all patients are retrieved.

        Returns:
            Response: JSON response containing patient data. Returns HTTP 200 status.
        """
        if patient_id:
            patient = get_object_or_404(Patient, pk=patient_id)
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            patients = Patient.objects.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST request to create a new patient.

        Args:
            request: HTTP request object containing patient data.

        Returns:
            Response: JSON response containing the created patient data if successful. Returns HTTP 201 status.
                      Returns JSON response with errors if the request data is invalid. Returns HTTP 400 status.
        """

        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            patient = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, patient_id):
        """
        Handle DELETE request to remove a patient.

        Args:
            request: HTTP request object.
            patient_id: ID of the patient to be deleted.

        Returns:
            Response: JSON response indicating the success of the operation. Returns HTTP 204 status.
        """

        patient = get_object_or_404(Patient, pk=patient_id)
        patient.delete()
        return Response(
            {"message": "Deletet successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class DoctorView(APIView):

    def get(self, request, doctor_id=None):
        """
        Handle GET request to retrieve doctor information.

        Args:
            request: HTTP request object.
            doctor_id: Optional ID of the doctor to retrieve. If not provided, all doctors are retrieved.

        Returns:
            Response: JSON response containing doctor data. Returns HTTP 200 status.
        """
        if doctor_id:
            doctor = get_object_or_404(Doctor, pk=doctor_id)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            doctors = Doctor.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST request to create a new doctor.

        Args:
            request: HTTP request object containing doctor data.

        Returns:
            Response: JSON response containing the created doctor data if successful. Returns HTTP 201 status.
                      Returns JSON response with errors if the request data is invalid. Returns HTTP 400 status.
        """

        serializer = DoctorSerializer(data=request.data)

        if serializer.is_valid():
            doctor = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, doctor_id):
        """
        Handle DELETE request to remove a doctor.

        Args:
            request: HTTP request object.
            doctor_id: ID of the doctor to be deleted.

        Returns:
            Response: JSON response indicating the success of the operation. Returns HTTP 204 status.
        """

        doctor = get_object_or_404(Doctor, pk=doctor_id)
        doctor.delete()
        return Response(
            {"message": "Deletet successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class AppointmentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, appointment_id=None):
        """
        Handle GET request to retrieve appointments.

        Args:
            request: HTTP request object.
            appointment_id: Optional ID of the appointment to retrieve. If not provided,
                            all appointments related to the requesting user are retrieved.

        Returns:
            Response: JSON response containing appointment data or error message.
        """

        user = request.user
        if appointment_id:
            appointment = get_object_or_404(Appointment, pk=appointment_id)
            if appointment.doctor.user == user or appointment.patient.user == user:
                serializer = AppointmentSerializer(appointment)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            appointments = Appointment.objects.filter(
                Q(doctor__user=user) | Q(patient__user=user)
            )
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST request to create a new appointment.

        Args:
            request: HTTP request object containing appointment data.

        Returns:
            Response: JSON response containing the created appointment data if successful.
                      Returns JSON response with errors if the request data is invalid.
        """

        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, appointment_id):
        """
        Handle DELETE request to delete an appointment.

        Args:
            request: HTTP request object.
            appointment_id: ID des zu löschenden Termins.

        Returns:
            Response: JSON response indicating success or failure of the delete operation.
        """

        appointment = get_object_or_404(Appointment, pk=appointment_id)
        appointment.delete()
        return Response(
            {"message": "Deletet successfully"}, status=status.HTTP_204_NO_CONTENT
        )

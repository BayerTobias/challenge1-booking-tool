from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)


class Doctor(models.Model):
    SPECIALITY_CHOICES = [
        ("allgemeinedizin", "Allgemeinedizin"),
        ("radiologe", "Radiologe"),
        ("hautarzt", "Hautarzt"),
    ]

    TITLE_CHOICES = [
        ("dr", "Dr."),
        ("prof_dr.", "Prof. Dr."),
        ("dr_rer_nat", "Dr. rer. nat"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20, choices=TITLE_CHOICES)
    speciality = models.CharField(max_length=50, choices=SPECIALITY_CHOICES)
    name = models.CharField(max_length=100, null=True)


class Appointment(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=250, default="")
    created_at = models.DateField(default=date.today)
    doctor = models.ForeignKey(Doctor, models.CASCADE)
    patient = models.ForeignKey(Patient, models.CASCADE)
    appointment_date = models.DateField(default=date.today)

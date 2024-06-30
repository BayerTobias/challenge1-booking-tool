"""
URL configuration for challenge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from booking_tool.views import LoginView, PatientView, DoctorView, AppointmentView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("api/patients/", PatientView.as_view(), name="patients"),
    path(
        "api/patients/<int:patient_id>/", PatientView.as_view(), name="patients_with_id"
    ),
    path("api/doctors/", DoctorView.as_view(), name="doctors"),
    path("api/doctors/<int:doctor_id>/", DoctorView.as_view(), name="doctors_with_id"),
    path("api/appointments/", AppointmentView.as_view(), name="appointments"),
    path(
        "api/appointments/<int:appointment_id>/",
        AppointmentView.as_view(),
        name="appointments_with_id",
    ),
]

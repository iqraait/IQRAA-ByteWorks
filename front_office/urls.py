from django.urls import path
from .views import PatientRegisterView,PatientsListView,LoadDoctorsView


app_name = 'front_office'  # Must have this namespace


urlpatterns = [
        path('', PatientRegisterView.as_view(), name="patient_register"),
        path("patients/", PatientsListView.as_view(), name="patients_list"),
        path('ajax/load-doctors/', LoadDoctorsView.as_view(), name='ajax_load_doctors'),


]
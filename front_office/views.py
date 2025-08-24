from django.views import View
from django.shortcuts import render, redirect
from .forms import PatientRegistrationForm, AddressForm
from .models import Patient_Registration,City
from django.views.generic import ListView
from django.http import JsonResponse


class PatientRegisterView(View):
    template_name = "front_office/patientregister.html"

    def get(self, request, *args, **kwargs):
        patient_form = PatientRegistrationForm()
        address_form = AddressForm()
        cities = City.objects.select_related("state__country").all()

        return render(request, self.template_name, {
            "patient_form": patient_form,
            "address_form": address_form,
            "cities":cities
        })

    def post(self, request, *args, **kwargs):
        patient_form = PatientRegistrationForm(request.POST)
        address_form = AddressForm(request.POST)

        if patient_form.is_valid() and address_form.is_valid():
            patient = patient_form.save()
            address = address_form.save(commit=False)
            address.patient = patient
            address.save()
            return redirect("front_office:patients_list")

        return render(request, self.template_name, {
            "patient_form": patient_form,
            "address_form": address_form,
        })



class PatientsListView(ListView):
    model = Patient_Registration
    template_name = "front_office/patients_list.html"
    context_object_name = "patients"
    ordering = ["-created"]  # latest first

    

class LoadDoctorsView(View):
    def get(self, request, *args, **kwargs):
        department_id = request.GET.get('department_id')
        if not department_id:
            return JsonResponse([], safe=False)  # return empty list if no department selected

        doctors = Doctor.objects.filter(department_id=department_id).values('id', 'name')
        return JsonResponse(list(doctors), safe=False)
from django import forms
from .models import Patient_Registration, Address

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient_Registration
        fields = [
            "mobile_number",
            "first_name",
            "middle_name",
            "whatapp_number",
            "date_of_birth",
            "gender",
            "patient_type",
            "title",
            "appoinment_date",
            "Department",
            "doctor_vist",
            "registration_type",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "appoinment_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["Address_line_1", "Address_line_2", "city", "state", "country", "pincode"]

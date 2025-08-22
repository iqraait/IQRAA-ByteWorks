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
            "department",
            "doctor_vist",
            "registration_type",
            "doctor_name"
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "appoinment_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["Address_line_1", "Address_line_2", "city", "state", "country", "pincode"]



# from django import forms
# from .models import Patient_Registration, Address

# class PatientRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Patient_Registration
#         fields = "__all__"
#         widgets = {
#             "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
#             "appoinment_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
#             "mobile_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "+91"}),
#             "first_name": forms.TextInput(attrs={"class": "form-control"}),
#             "middle_name": forms.TextInput(attrs={"class": "form-control"}),
#             "whatapp_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "+91"}),
#             "gender": forms.Select(attrs={"class": "form-select"}),
#             "patient_type": forms.Select(attrs={"class": "form-select"}),
#             "title": forms.Select(attrs={"class": "form-select"}),
#             "Department": forms.Select(attrs={"class": "form-select"}),
#             "doctor_vist": forms.Select(attrs={"class": "form-select"}),
#             "registration_type": forms.Select(attrs={"class": "form-select"}),
#             "doctor_name": forms.Select(attrs={"class": "form-select"}),
#         }

# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = "__all__"
#         exclude = ["patient"]  # because patient will link after saving
#         widgets = {
#             "Address_line_1": forms.TextInput(attrs={"class": "form-control"}),
#             "Address_line_2": forms.TextInput(attrs={"class": "form-control"}),
#             "city": forms.TextInput(attrs={"class": "form-control"}),
#             "state": forms.TextInput(attrs={"class": "form-control"}),
#             "country": forms.Select(attrs={"class": "form-select"}),
#             "pincode": forms.TextInput(attrs={"class": "form-control"}),
#         }

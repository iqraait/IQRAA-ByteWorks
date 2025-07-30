# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Employee,Department



"""Employee RegistrationFrom"""

class EmployeeRegistrationForm(UserCreationForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=True,
        label="Department"
    )
    
    class Meta:
        model = Employee
        fields = ('iqraa_id', 'department', 'password1', 'password2')  # how the form will be set order wise
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['iqraa_id'].label = "Iqraa ID"
        self.fields['iqraa_id'].help_text = "Your unique employee identification number"
        self.fields['password1'].help_text = None



"""Employee Login Form"""

class EmployeeLoginForm(AuthenticationForm):
    username = forms.IntegerField(
        label="Iqraa ID",
        widget=forms.NumberInput(attrs={'autofocus': True}))
    
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput)
    
    error_messages = {
        'invalid_login': "Invalid Iqraa ID or password.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Iqraa ID'
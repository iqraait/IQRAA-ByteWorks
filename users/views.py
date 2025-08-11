
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import EmployeeLoginForm,EmployeeRegistrationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,authenticate
from django.urls import reverse_lazy
from .models import Employee
from django.contrib import messages






class EmployeeRegistrationView(View):
    template_name = 'users/register.html'
    form_class = EmployeeRegistrationForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        

        if form.is_valid():
            # Print cleaned data (after validation)
            print("\n=== Cleaned Form Data ===")
            for key, value in form.cleaned_data.items():
                print(f"{key}: {value}")

            # Save the form and redirect
            form.save()
            return redirect(self.success_url)
        else:
            # Print form errors if validation fails
            print("\n=== Form Errors ===")
            for field, errors in form.errors.items():
                print(f"{field}: {errors}")

        return render(request, self.template_name, {'form': form})






"""Class for the First DashBoard View opening url"""

class FirstDashBoard(TemplateView):
    template_name = 'users/main_dashboard.html'




class EmployeeLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = EmployeeLoginForm

    REDIRECT_MAPPING ={
        (True,'NURSING_DEPARTMENT'):('nursing_department','NursingAdminDashboard'),
        (False,'NURSING_DEPARTMENT'):('nursing_department','staffdashboard')
    }


    DEFAULT_REDIRECT = ('users','main_dashboard')

    def get_redirect_info(self,user):
        """Direct database lookup without caching"""
        if not user.department:
            return self.DEFAULT_REDIRECT

        department_name = user.department.department_name
        return self.REDIRECT_MAPPING.get((user.is_staff,department_name),self.DEFAULT_REDIRECT)


    def get_success_url(self):
        user = self.request.user
        app_name,url_name = self.get_redirect_info(user)
        url = reverse_lazy(f'{app_name}:{url_name}')
        return url































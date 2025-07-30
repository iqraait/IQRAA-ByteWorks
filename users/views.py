
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








"""class for the LoginView with iqraa_id & password"""

class EmployeeLoginView(LoginView):
    redirect_authenticated_user = True  # if set True this will automatically logged user away from the login page when try to access
    form_class = EmployeeLoginForm      # login form inside the forms.py
    template_name = 'users/login.html' 


    def form_invalid(self, form):     # build in function for form data checking
        messages.error(self.request, 'Invalid Credentials')
        return self.render_to_response(self.get_context_data(form=form))       

    def get_success_url(self):
        return ('register') 


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self._redirect_authenticated_user(request.user)
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            iqraa_id = form.cleaned_data['iqraa_id']
            password = form.cleaned_data['password']
            user = authenticate(request, username=iqraa_id, password=password)
            
            if user is not None:
                login(request, user)
                return self._redirect_authenticated_user(user)
            else:
                form.add_error(None, "Invalid Iqraa ID or password")
        
        return render(request, self.template_name, {'form': form})
    

    def _redirect_authenticated_user(self, user):
        if user.is_superuser:
            return redirect('admin_panel')
        elif not user.is_staff and hasattr(user, 'department'):
            if user.department.name == "Nursing_station":
                return redirect('nursing_station:dashboard')
        # Add more conditions for other departments as needed
        return redirect('default_dashboard')  # Fallback for other users
    










# """class after staff login""",]


# class userDashboardView(TemplateView):
#     template_name = 'users/user_dashboard.html'
#     def dispatch(self, request, *args, **kwargs):
#         # Restrict access to only logged-in staff
#         if not request.user.is_authenticated or not request.user.is_staff:
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)
    



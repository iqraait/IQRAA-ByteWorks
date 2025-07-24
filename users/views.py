
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import EmployeeLoginForm,EmployeeRegistrationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.urls import reverse_lazy



"""View for the Register a user/admin_access staff"""

class EmployeeRegistrationView(View):  
    template_name = 'users/register.html'
    form_class = EmployeeRegistrationForm
    success_url = reverse_lazy('login')  # Add this line

    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login') 
        return render(request, self.template_name, {'form': form})



"""Class for the First DashBoard View opening url"""

class FirstDashBoard(TemplateView):
    template_name = 'users/main_dashboard.html'



"""class for the LoginView with iqraa_id & password"""

class EmployeeLoginView(LoginView):
    form_class = EmployeeLoginForm
    template_name = 'users/login.html' 
    success_message = "Your account was created successfully!"
    success_url = reverse_lazy('dashboard_afterlogin')  



    def form_valid(self, form):
        # Custom logic if needed before login
        return super().form_valid(form)



class DashboardView(TemplateView):
    template_name = 'users/dashboard_after_login.html'

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Employee
from django.contrib import messages


def dashboard_view(request):
    return render(request, 'users/dashboard.html')



def login_view(request):
    






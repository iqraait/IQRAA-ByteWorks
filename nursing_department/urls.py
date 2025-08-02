from django.urls import path
from .views import StaffDashboard,StaffDashBoardForAdmin

app_name = 'nursing_department'  # Must have this namespace



urlpatterns = [

        path('staffDashB0ard',StaffDashboard.as_view(),name='staffdashboard'),
        path('NursingAdminDashB0ard',StaffDashBoardForAdmin.as_view(),name='NursingAdminDashboard')

]










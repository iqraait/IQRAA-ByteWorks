from django.urls import path
from .views import StaffDashboard,StaffDashBoardForAdmin,TestingForm,PreviewForm

app_name = 'nursing_department'  # Must have this namespace



urlpatterns = [

        path('staffDashB0ard',StaffDashboard.as_view(),name='staffdashboard'),
        path('NursingAdminDashB0ard',StaffDashBoardForAdmin.as_view(),name='NursingAdminDashboard'),
        path('preview',PreviewForm.as_view(),name="form2"),
        path('form3',TestingForm.as_view(),name='form3')
]











from django.urls import path
from .views import StaffDashboard,AdminDashboardView,TestingForm,PreviewForm,DownloadPdf,AdminDashboardView

app_name = 'nursing_department'  # Must have this namespace



urlpatterns = [

        path('staffDashB0ard',StaffDashboard.as_view(),name='staffdashboard'),
        path('preview',PreviewForm.as_view(),name="form2"),
        path('form3',TestingForm.as_view(),name='form3'),
        path("admin_dashboard/", AdminDashboardView.as_view(), name="nursing_admin_dashboard"),
        path("admin-dashboard/download/<int:pk>/", DownloadPdf.as_view(), name="download_assessment"),
        path("admin-dashboard/approve/<int:pk>/", AdminDashboardView.as_view(), name="approve_assessment"),



]











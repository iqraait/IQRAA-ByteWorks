
from django.views.generic import TemplateView



class StaffDashboard(TemplateView):
    template_name = 'nursing_admin/MainFormForAllStaf.html'



class StaffDashBoardForAdmin(TemplateView):
    template_name = 'nursing_admin/DashBoardForAdminAccess.html'
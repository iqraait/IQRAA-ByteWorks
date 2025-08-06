from django.views.generic import TemplateView



class StaffDashboard(TemplateView):
    template_name = 'nursing_admin/MainFormForAllStaf.html'

    forms_dictionary = {
        'form1':'nursing_admin/form1.html',
        'form2':'nursing_admin/form2.html',
        'form3':'nursing_admin/from3.html'
    }
    




class StaffDashBoardForAdmin(TemplateView):
    template_name = 'nursing_admin/DashBoardForAdminAccess.html'


class FormViewClass(TemplateView):
    template_name = 'nursing_admin/form1.html'
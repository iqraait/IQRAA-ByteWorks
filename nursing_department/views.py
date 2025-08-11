from django.views.generic import TemplateView
from .forms import NicuForm,NicuFormAssementData
from django.contrib import messages
from django.shortcuts import redirect, render
from .constants_data import FORM1_FULL_STRUCTURE




class StaffDashboard(TemplateView):
    template_name = 'nursing_admin/MainFormForAllStaf.html'



class StaffDashBoardForAdmin(TemplateView):
    template_name = 'nursing_admin/DashBoardForAdminAccess.html'



class TestingForm(TemplateView):
    template_name = "nursing_admin/form3.html"



class PreviewForm(TemplateView):
    template_name = "nursing_admin/from2.html"
    success_url = "nursing_department:form3"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form1'] = NicuForm(prefix='form1')  # Note: Don't instantiate with () in class attribute
        context['form2'] = NicuFormAssementData(prefix='form2')
        
        return context
    
    def post(self,request,*args,**kwargs):
        form1 = NicuForm(request.POST,prefix = "form1")
        # form2 = NicuFormAssementData(request.POST,prefix = "form2")

        if form1.is_valid():
            instance1 = form1.save()
        
            messages.success(request, "Form submitted successfully!")

            return redirect(self.success_url)
    
        return render(request,self.template_name,{'form1':form1}
)


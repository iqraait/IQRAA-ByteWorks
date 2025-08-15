from django.views.generic import TemplateView
from .forms import NicuForm,NicuFormAssementData
from django.contrib import messages
from django.shortcuts import redirect, render
# from .constants_data import FORM1_FULL_STRUCTURE
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee




class StaffDashboard(LoginRequiredMixin,TemplateView):
    template_name = 'nursing_admin/MainFormForAllStaf.html'



class StaffDashBoardForAdmin(LoginRequiredMixin,TemplateView):
    template_name = 'nursing_admin/DashBoardForAdminAccess.html'



class TestingForm(TemplateView):
    template_name = "nursing_admin/form3.html"



class PreviewForm(LoginRequiredMixin,TemplateView):
    template_name = "nursing_admin/from2.html"
    success_url = "nursing_department:form3"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form1'] = NicuForm(prefix='form1')  # Note: Don't instantiate with () in class attribute
        context['form2'] = NicuFormAssementData(prefix='form2')
        
        return context
    
    def post(self, request, *args, **kwargs):
        form1 = NicuForm(request.POST, prefix="form1")  # Staff form
        form2 = NicuFormAssementData(request.POST, prefix="form2")  # Assessment form



        if form1.is_valid() and form2.is_valid():

            staff_instance = form1.save()
            print("\n=== Cleaned Form Data Form1 ===")
            for key, value in form1.cleaned_data.items():
                print(f"{key}: {value}")


            print("\n=== Cleaned Form Data ===")
            for key, value in form2.cleaned_data.items():
                print(f"{key}: {value}")

                
            # Get evaluator from logged-in user
            evaluator_instance = request.user

            # Save assessment using form's save method
            form2.save(staff=staff_instance, evaluator=evaluator_instance)

            messages.success(request, "Form submitted successfully!")
            return redirect(self.success_url)

        return render(request, self.template_name, {
            'form1': form1,
            'form2':form2
        })



from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

class AdminDashboardView(LoginView):
    template_name = 'nursing_admin/admin_dashboard.html'

    def test_func(self):
        return self.request.user.is_superuser
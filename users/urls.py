from django.urls import path
from .views import FirstDashBoard,EmployeeLoginView,EmployeeRegistrationView
# from .views import userDashboardView
from .views import NsForm1View

urlpatterns = [
        path('', FirstDashBoard.as_view(), name='main_dashboard'),  # main dshboard url
        path('login/', EmployeeLoginView.as_view(), name='login'),  # login url
        path('register/', EmployeeRegistrationView.as_view(), name='register'), # new user registraion url
        # path('user_dashboard', userDashboardView.as_view(), name='user_dashboard'),
        path('ns_form1/', NsForm1View.as_view(), name='ns_form1'),





]
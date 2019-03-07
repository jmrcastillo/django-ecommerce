

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as acounts_views
from .forms import AuthenticationForm


app_name = 'accounts'

urlpatterns = [
        path('login/', auth_views.LoginView.as_view(
                                                template_name='user_accounts/login.html',
                                                authentication_form=AuthenticationForm), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='user_accounts/logout.html'), name='logout'),
        path('signup/', acounts_views.signup, name='signup'),
]

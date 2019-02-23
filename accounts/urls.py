

from django.contrib.auth.views import login, logout
from django.urls import path
from . import views
from .forms import AuthenticationForm


app_name = 'accounts'

urlpatterns = [
        path(r'login/', login, {
            'template_name': 'user_accounts/login.html',
            'authentication_form': AuthenticationForm
            }, name='login'),
        path(r'logout/', logout, {
            'next_page': '/'
            }, name='logout'),
        path(r'signup/', views.signup, name='signup'),
]

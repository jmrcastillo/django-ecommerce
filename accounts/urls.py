

from django.contrib.auth.views import login, logout
from django.urls import path
from . import views
from .forms import AuthenticationForm

urlpatterns = [
        path(r'', views.index, name='index'),
        path(r'accounts/login/', login, {
            'template_name': 'user_accounts/login.html',
            'authentication_form': AuthenticationForm
            }, name='login'),
        path(r'accounts/logout', logout, {
            'next_page': '/'
            }, name='logout'),
        path(r'accounts/signup', views.signup, name='signup'),
]

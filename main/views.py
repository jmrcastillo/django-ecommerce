

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import SignupForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'main/create_account_success.html', {})
    # return render(request, 'main/index.html', {})


@csrf_protect
def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
            )
            user.save()

            return render(request, 'main/create_account_success.html', {})

    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})

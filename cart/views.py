

from django.shortcuts import render


def cart_home(request):
    # request.session.set_expiry(300)
    # key = request.session.session_key
    # print(key)
    request.session['first_name'] = "Mau"
    return render(request, "cart/home.html", {})

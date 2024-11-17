from django.shortcuts import render

def test_template(request):
    return render(request, "allauth/account/login.html")

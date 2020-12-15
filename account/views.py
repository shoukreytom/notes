from django.shortcuts import render


def signup(request):
    return render(request, 'account/register.html')

def signin(request):
    return render(request, 'account/login.html')

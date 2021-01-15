from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .models import Account


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password1 = request.POST.get('password1', None)
        password12 = request.POST.get('password2', None)
        if not (email is None and password1 != password12):
            account = Account(email=email)
            account.set_password(password12)
            account.save()
            return redirect('signin')
    return render(request, 'account/signup.html')

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'account/signin.html')

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Account
from home.models import Note


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
    next_url = request.GET.get('next', '')
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            # TODO: parse path to redirect user to specified path
            next_url = request.POST.get('next')
            if next_url != '':
                return redirect(next_url)
            return redirect('home')
    return render(request, 'account/signin.html', {'next': next_url})

@login_required
def profile(request):
    user = request.user
    count_notes = Note.objects.filter(author=user).count()
    ctx = {
        'user': user,
        'notes_num': count_notes,
    }
    return render(request, 'account/profile.html', ctx)

@login_required
def signout(request):
    logout(request)
    return redirect('home')

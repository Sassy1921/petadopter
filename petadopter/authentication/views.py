import email
import uuid
from email import message
import imp
from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from authentication.forms import RegistrationForm, AccountAuthenticationForm
from authentication.models import Account
from django.contrib import messages
from petadopter import settings



def adoption(request):
    return render(request,'authentication/adoption.html',{})
def signout(request):
    logout(request)
    messages.success(request,' You logged out succesfully!')
    return redirect('home')
def signup(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password=form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            account.save()
            messages.success(request,' Congrats, Your account was created succesfully!, please log in')
            return redirect('home')

        else:
            context['registration_form'] = form
    else:
        form=RegistrationForm()
        context['registration_form'] = form
    return render(request,'authentication/signup.html',context)
def signin(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form=AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user = authenticate(email=email,password=password)

            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"account doesen't exist plz sign in")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request,'authentication/signin.html',context)




import email
from email import message
import imp
from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from authentication.forms import RegistrationForm, AccountAuthenticationForm
from authentication.models import Account
from django.contrib import messages
from petadopter import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.utils.encoding import force_bytes,force_text
from django.template.loader import render_to_string

def signout(request):
    logout(request)
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
            messages.success(request,'congrats, Your account was created succesfully!')
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

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        account = None
    if account is not None and account_activation_token.check_token(account, token):
        account.is_active = True
        account.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



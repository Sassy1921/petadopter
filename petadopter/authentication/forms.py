from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from authentication.models import Account
FAMILIAL_STATUS_CHOICES = (
    ('Married',"married"),
    ('Divorced','divorced'),
    ('Separated','separated'),
    ('Single','single'),
    ('Widow(er)','widow(er)')
)
LODGING_CHOICES = (
    ('With Garden', 'with garden'),
    ('Without Garden', 'without garden'),

)
class RegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=60,help_text='Required. Add a valid email address')
    class Meta:
        model = Account
        fields=("email","username","first_name","last_name","cin","salary","phone_number","password1","password2","lodging","fammilial_status")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email','password')
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
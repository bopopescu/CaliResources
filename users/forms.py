from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from .models import Profile , Language , Disability

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username','email','password1','password2']
        
class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField()
    class Meta:
            model = User
            fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
            model = Profile
            fields  = ['firstname','lastname','phone','country','bornDate','image']
class ProfileLanguageForm(forms.ModelForm):
     class Meta:
            model = Language 
            fields = ['language']
class ProfileDisabilityForm(forms.ModelForm):
    class Meta: 
            model = Disability
            fields = ['disability']

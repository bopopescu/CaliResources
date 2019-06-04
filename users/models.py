from django.db import models
from django.contrib.auth.models import User 
from PIL import Image
from languages.fields import LanguageField
from django_countries.fields import CountryField
import datetime
from phone_field import PhoneField
class Language(models.Model): 
    language = LanguageField()
   
    def __str__(self):
        return self.language
class Disability (models.Model):
    disability = models.CharField(max_length=255)
  
    def __str__(self):
        return self.disability
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255, default='nombre')
    lastname = models.CharField(max_length=255, default='apellido')
    phone = PhoneField(blank=True, help_text='Numero de Celular')
    country = CountryField(default='mexico')
    bornDate = models.DateField('Fecha de nacimiento',blank=False,default=datetime.date.today)
    image  = models.ImageField(default='default.png',upload_to='profile_pics')
    disability = models.ManyToManyField(Disability)
    language = models.ManyToManyField(Language)
  
    def __str__(self):
        return f'{self.user.username} Profile'




    
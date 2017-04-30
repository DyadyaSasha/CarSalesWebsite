from django import forms
from .models import Car, Order
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

class CarForm(forms.ModelForm):

    class Meta:
        model=Car
        fields = ('firm','model', 'price', 'type_of_transmission','image',)

class RegisterForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields = ('username', 'password', 'email',)

class LoginForm(forms.ModelForm):

    class Meta:
        model=User
        fields=('username', 'password',)
        
# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model=Acount
#         fields = ('login', 'password', 'email', 'name', 'lastname',)
    
#     def save(self):
#         pass


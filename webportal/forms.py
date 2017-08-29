from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import Support

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class SupportForm(forms.ModelForm):
	class Meta:
		model = Support
		fields = ['assunto']
		labels = {'Assunto': ''}

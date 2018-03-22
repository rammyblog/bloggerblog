from django import forms
from .models import Blogpost
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
	class Meta:
		model = Blogpost
		fields = ['title','content','tags']
		widgets = {'title': forms.TextInput(attrs = {'input class':"large", 'type':"text", 'name':"input", 'required':"required"}), }
class Register(UserCreationForm):
	first_name= forms.CharField(max_length = 50,)
	last_name= forms.CharField(max_length = 50,)
	email=forms.EmailField(max_length = 100, help_text = 'Enter a valid E-mail Address')
	class Meta:
		model = User
		fields = ['username','email', 'first_name', 'last_name', 'password1', 'password2']
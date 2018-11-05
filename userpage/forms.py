# -*- coding: utf-8 -*-
from django import forms
# from .models import Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import CustomUser
from question.models import Post

class SettingForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = [ 'avatar', 'city', 'username', 'first_name', 'last_name']
        #exclude = ()model

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)



from django import forms
from IOT_Users.models import *

from django.contrib.auth.models import User

class IOTUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email']

class IOTUserProfileForm(forms.ModelForm):
	class Meta:
		model = IOTUser
		fields = ['user','user_type']
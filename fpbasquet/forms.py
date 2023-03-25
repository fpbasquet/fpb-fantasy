from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	date_of_birth = forms.DateField(required=True,widget=forms.DateInput(attrs={'type':'date','max':datetime.date.today()}))
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

User = get_user_model()

from .models import Profile


class UserRegistrationForm(forms.ModelForm):
	email = forms.EmailField(label='Email Address')
	email2 = forms.EmailField(label='Confirm Email')
	password = forms.CharField(max_length=25,widget=forms.PasswordInput)
	class Meta:
		model = User 
		fields = [
			'first_name',
			'last_name',
			'username',
			'email',
			'email2',
			'email',
			'password',
		]

	def clean(self,*args,**kwargs):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Emails dont match !")
		
		email_qs = User.objects.filter(email=email)
		if email_qs.exists() or email_qs.count() != 0:
			raise forms.ValidationError("This email already exists")
		return super(UserRegistrationForm,self).clean(*args, **kwargs)


class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=120)
	password = forms.CharField(max_length=25,widget=forms.PasswordInput)


	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		
		if username and password:
			user_qs = User.objects.filter(username=username)
			if user_qs.count() == 0 or user_qs.count() != 1:
				raise forms.ValidationError("Username doesn't match")
			else:
				user = user_qs.first()
			if not user.check_password(password):
				raise forms.ValidationError("Password doesn't match")
			return super(UserLoginForm,self).clean(*args,**kwargs)

class ProfileForm(forms.ModelForm):
	DOY = ('1975','1976','1977','1978','1979','1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015','2016','2017')
	birth_date = forms.DateField(widget=forms.SelectDateWidget(years=DOY))
	height = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter in Centimeters.'}))
	class Meta:
		model = Profile
		fields = [
				'phone_no',
				'birth_date',
				'gender',
				'bio',
				'marital_status',
				'religion',
				'qualification',
				'height',
				'latitude',
				'longitude',
				]


class LocationForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['latitude','longitude']


















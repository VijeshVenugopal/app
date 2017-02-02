from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField



class SignupForm(forms.Form):

	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	captcha = NoReCaptchaField()

	def clean(self):
		form_data=self.cleaned_data
		print form_data
		return form_data




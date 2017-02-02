from django import forms
from data.models import *
from django.contrib.auth.models import User
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})



class TicketForm(forms.ModelForm):
	
	status = forms.ModelChoiceField(queryset=TicketStatus.objects.all(),widget = forms.Select(attrs={'class':'selectpicker','title':'Choose one of the following.'}))
	type = forms.ModelChoiceField(queryset=TicketType.objects.all(),widget = forms.Select(attrs={'class':'selectpicker'}))
	priority = forms.ModelChoiceField(queryset=TicketPriority.objects.all(),widget = forms.Select(attrs={'class':'selectpicker'}))
	assign = forms.ModelChoiceField(queryset= User.objects.filter(is_staff=1),widget = forms.Select(attrs={'class':'selectpicker'}))
	file = forms.FileField(required=False)

	class Meta:
		model = Ticket
		fields = ('title','status','type','priority','assign')

	def clean(self):
		form_data=self.cleaned_data
		#print form_data
		return form_data

class TicketDetailForm(forms.ModelForm):

	class Meta:
		model = TicketDetail
		fields = ('ticket_text',)

	def clean(self):
		form_data=self.cleaned_data
		#print form_data
		return form_data

	#widgets = forms.Select(attrs={'class':'selectpicker'})

class TicketEditForm(forms.ModelForm):

	status = forms.ModelChoiceField(queryset=TicketStatus.objects.all(),widget = forms.Select(attrs={'class':'selectpicker','title':'Choose one of the following.'}))
	type = forms.ModelChoiceField(queryset=TicketType.objects.all(),widget = forms.Select(attrs={'class':'selectpicker'}))
	priority = forms.ModelChoiceField(queryset=TicketPriority.objects.all(),widget = forms.Select(attrs={'class':'selectpicker'}))
	assign = forms.ModelChoiceField(queryset= User.objects.filter(is_staff=1),widget = forms.Select(attrs={'class':'selectpicker'}))
	file = forms.FileField(required=False)

	class Meta:
		model = Ticket
		fields = ('status','type','priority','assign')

	def clean(self):
		form_data=self.cleaned_data
		#print form_data
		return form_data

class ForgotPasswordForm(forms.Form):
	email = forms.EmailField(required=True)

	def clean(self):
		form_data = self.cleaned_data
		return form_data

class ResetPasswordForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput())

	def clean(self):
		form_data = self.cleaned_data
		return form_data

class PropertyForm(forms.ModelForm):
	
	status = forms.ModelChoiceField(queryset=TicketStatus.objects.all(),required=False,widget = forms.Select(attrs={'class':'selectpicker'}))
	type = forms.ModelChoiceField(queryset=TicketType.objects.all(),required=False,widget = forms.Select(attrs={'class':'selectpicker'}))
	priority = forms.ModelChoiceField(queryset=TicketPriority.objects.all(),required=False,widget = forms.Select(attrs={'class':'selectpicker'}))
	start_date = forms.DateField(widget=DateInput(),required=False)
	end_date = forms.DateField(widget=DateInput(),required=False) 

	class Meta:
		model = Ticket
		fields = ('status','type','priority')

	def clean(self):
		form_data=self.cleaned_data
		#print form_data
		return form_data

class TicketListForm(forms.ModelForm):
	user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=0,is_active=1),required=False,widget = forms.Select(attrs={'class':'selectpicker'}))
	status = forms.ModelChoiceField(queryset=TicketStatus.objects.all(),required=False,widget = forms.Select(attrs={'class':'selectpicker'}))
	id = forms.CharField(max_length=100,required=False)
	username = forms.CharField(max_length=100,required=False)

	class Meta:
		model = User
		fields = ('id','username','user','status')

	def clean(self):
		form_data=self.cleaned_data
		#print form_data
		return form_data

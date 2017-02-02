from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View,CreateView, UpdateView
from django.contrib.auth.models import User
from .SignupForm import *
from django.http import HttpResponse,HttpResponseRedirect
from data.models import *
from .TicketForm import *
from django.core.urlresolvers import reverse
from datetime import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.template import Context, Template, RequestContext
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib import messages






'''@login_required()
def tickets_create(request):
	return render(request,"tickets_create.html")'''

class CreateTicket(CreateView):
	form_class1 = TicketForm
	form_class2 = TicketDetailForm
	template_name = "tickets_create.html"

	def get(self,request,*args,**kwargs):
		return render(request,self.template_name,{'form1':self.form_class1,'form2':self.form_class2})
	

	def get_success_url(self):
		return HttpResponseRedirect(reverse('tickets'))


	def post(self,request,*args,**kwargs):
		form1 = self.get_form(self.form_class1)
		form2 = self.get_form(self.form_class2)

		if form1.is_valid() and form2.is_valid():
			
			#fpath = 'static/mymedia/' + str(datetime.now()) + file.name
			print "form is valid"
			data1 = form1.cleaned_data
			data2 = form2.cleaned_data
			print data1, data2
			obj1 = form1.save(commit=False)
			obj1.assigned_user_id = data1['assign'].id
			obj1.created_user_id = self.request.user.id
			obj1.save()
			obj2 = form2.save(commit=False)
			obj2.ticket = obj1
			obj2.status = obj1.status
			obj2.created_user_id = self.request.user.id
			obj2.save()
			if request.FILES:
				file = request.FILES['file']
				print file
				fname = str(datetime.now()) + file.name
				fpath = '/home/suyati/jango_pro/ticketingPro/static/mymedia/' + fname
				get_path = 'static/mymedia/' + fname
				handle_uploaded_file(file,fpath)
				attachment = TicketAttachment()
				attachment.file_name=get_path
				attachment.ticket = obj1
				attachment.ticket_detail = obj2
				attachment.original_file_name = file.name
				attachment.created_user_id = request.user.id
				attachment.save()
			msg_head = "New Ticket:"+obj1.title
			msg_body = "Ticket Detail: "+obj2.ticket_text
			email = EmailMessage(msg_head, msg_body, to=[data1['assign'].email])
			email.send()

			
			

			return self.get_success_url()

		else:
			print "form not valid"
			return render(request,self.template_name,{'form1':form1,'form2':form2})

def handle_uploaded_file(file,filepath):
	with open(filepath, 'wb+') as destination:
		for chunk in file.chunks():
			destination.write(chunk)
				


class EditTicket(UpdateView):
	form1 = TicketEditForm
	form2 = TicketDetailForm
	template_name = "ticket_edit.html"

	def get_object(self):
		id = self.kwargs['pk']
		ticket_obj = Ticket.objects.get(ticket_id=id)
		return ticket_obj

	def get_initial(self):
		initial = super(EditTicket, self).get_initial()
		thisticket = self.get_object()
		thisuser = User.objects.get(id=thisticket.assigned_user_id)
		initial['assign'] = thisuser
		created_user = User.objects.get(id=thisticket.created_user_id)
		initial['created'] = created_user
		ticket_detail = thisticket.ticketdetail_set.all()
		ticket_file = thisticket.ticketattachment_set.all()
		initial['ticket_file'] = ticket_file

		detail_list=[]
		count = 0
		for detail in ticket_detail:
			detail_dict={}
			obj_user = User.objects.get(id=detail.created_user_id) 
			detail_dict['user_name'] = obj_user.first_name.capitalize() + ' ' + obj_user.last_name.capitalize()
			detail_dict['ticket_text'] = detail.ticket_text
			detail_dict['ticket_detail_id'] = detail.ticket_detail_id
			detail_dict['created_date_time'] = detail.created_date_time
			detail_dict['status'] = detail.status
			detail_dict['files'] = detail.ticketattachment_set.filter(ticket_detail_id=detail.ticket_detail_id)
 			detail_list.append(detail_dict)
 			count += 1
 		detail_list[count-1]['style'] = "in"
		detail_list.reverse()
		initial['detail'] = detail_list
		return initial

	def get(self,request,*args,**kwargs):
		form1 = self.form1(instance=self.get_object(), initial=self.get_initial())
		#ticket_detail_obj = TicketDetail.objects.get(ticket=self.get_object())
		return render(request,self.template_name,{'form1':form1,'form2':self.form2,'myticket':self.get_object,'initial':self.get_initial()})

	def post(self,request,*args,**kwargs):
		form1 = self.form1(request.POST,instance=self.get_object(), initial=self.get_initial())
		form2 = self.get_form(self.form2)
		if form1.is_valid() and form2.is_valid():
			obj1 = form1.save()
			obj2 = form2.save(commit=False)
			obj2.ticket = obj1
			obj2.status = obj1.status
			obj2.created_user_id = self.request.user.id
			obj2.save()
			#sending mail
			if(str(obj1.status) == "Completed"):
				user = User.objects.get(id=obj1.created_user_id)
				msg_head = "Ticketing System: "+obj1.title
				msg_body = "Ticket Closed: "+obj2.ticket_text
				email = EmailMessage(msg_head, msg_body, to=[user.email])
				email.send()
			else:
				if request.user.is_staff :
					user = User.objects.get(id=obj1.created_user_id)
					msg_head = "Ticketing System: "+obj1.title
					msg_body = "Comment: "+obj2.ticket_text
					email = EmailMessage(msg_head, msg_body, to=[user.email])
					email.send()
			if request.FILES:
				file = request.FILES['file']
				#fpath = 'static/mymedia/' + str(datetime.now()) + file.name
				fname = str(datetime.now()) + file.name
				fpath = '/home/suyati/jango_pro/ticketingPro/static/mymedia/' + fname
				get_path = 'static/mymedia/' + fname
				handle_uploaded_file(file,fpath)
				attachment = TicketAttachment()
				attachment.file_name=get_path
				attachment.ticket = obj1
				attachment.ticket_detail = obj2
				attachment.original_file_name = file.name
				attachment.created_user_id = request.user.id
				attachment.save()
				print "form with file"
			else:
				print "no file"
			return HttpResponseRedirect(reverse('tickets'))
		return render(request,self.template_name,{'form1':form1,'form2':self.form2,'myticket':self.get_object,'initial':self.get_initial(),'error':'error'})




class SignupView(View):
	model = User
	form_class = SignupForm
	template_name = "signup.html"

	def get(self,request,*args,**kwargs):
		return render(request,self.template_name, {'form' : self.form_class})

	def post(self,request,*args,**kwargs):
		form = SignupForm(request.POST)
		
		if form.is_valid():

				print "new user"
				new_user = User.objects.create_user(
					username = form['email'].value(),
					first_name = form['first_name'] .value(),
					last_name = form['last_name'].value(),
					email = form['email'].value(),
					password = form['password'].value(),
					is_staff = 0,
					is_active = 1,
					is_superuser = 0
					)
				new_user.save()
				#return render(request,self.template_name, {'form' : self.form_class})
				messages.add_message(request, messages.SUCCESS, "signup")
				return HttpResponseRedirect(reverse('login'))
		return render(request,self.template_name, {'form' : form})


class ForgotPassword(View):
	template_name = "forgotpassword.html"
	form_class = ForgotPasswordForm

	def get(self,request,*args,**kwargs):
		return render(request,self.template_name)

	def post(self,request,*args,**kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data
			email = form_data['email']
			is_valid_email = User.objects.filter(username=email,is_active=True).exists()
			if is_valid_email:
				uuid = ResetPassword()
				uuid.email = email
				uuid.save()
				print "saved"
				uuid_code = uuid.reset_code
				link = "http://ticket.com/forgotpassword/reset/" + str(uuid_code)
				# html_message = loader.render_to_string(
		  #           'emailbody.html',
		  #           {
		  #               'link': link,
		                 
		  #           }
		  #       )
				msg_head = "Ticketing System Password reset link"
				msg_body = "Click on the Link to reset the password " + link
				email = EmailMessage(msg_head, msg_body, to=[email])
				email.send()
				messages.add_message(request, messages.INFO, "forgot")
				return HttpResponseRedirect(reverse('login'))
			else:
				print "Invalid User"
				return render(request,self.template_name,{'errors':email})
		return render(request,self.template_name)


class ResetPasswordView(View):
	template_name = "reset.html"
	form_class = ResetPasswordForm

	def get(self,request,*args,**kwargs):
		uuid_code = self.kwargs['uuid']
		print "uuid_code",uuid_code
		try:
			if not ResetPassword.objects.get(reset_code=uuid_code,deleted=False) :
				return render(request,self.template_name)
		except:
			return HttpResponseRedirect(reverse('login'))
		return render(request,self.template_name)
			
			
		

	def post(self,request,*args,**kwargs):
		form = self.form_class(request.POST)
		uuid_code = self.kwargs['uuid']
		if form.is_valid():
			form_data = form.cleaned_data
			password =  form_data['password']
			reset_obj = ResetPassword.objects.get(reset_code=uuid_code,deleted=False)
			#if reset_obj.created_date_time
			email =  reset_obj.email
			user_obj = User.objects.get(username=email,is_active=1)
			user_obj.set_password(password)
			#print user_obj.password
			user_obj.save()
			reset_obj.deleted = True
			reset_obj.save()
			return HttpResponseRedirect(reverse('login'))
		return HttpResponse(0)


def ticket_formating(ticket):	
		# print "*********************************************"
		try:		
			fmt = '%Y-%m-%d'	
			current_date = datetime.now().strftime(fmt)	
			current_date = datetime.strptime(current_date, fmt)	
			# print "*********************************************"	
			# print 'current_date',current_date		
			for each_item in ticket:
				# print "*********************************************"			
				created_date = each_item.created_date_time.strftime(fmt)			
				created_date = datetime.strptime(created_date, fmt)			
				#print 'created_date',created_date			
				num_days = (current_date-created_date).days		

				# print 'num_days',num_days			
				if num_days>=7:				
					each_item.color="danger"			
				elif num_days>=3:				
					each_item.color="warning"			
				else:				
					each_item.color="success"	
				
		except:
			pass	
		return ticket

class ReportView(View):
	template_name = "report.html"
	form1 = PropertyForm

	

	def get(self,request,*args,**kwargs):
		if not request.user.is_staff:
			is_tickets=Ticket.objects.filter(created_user_id=request.user.id).exists()
			if  is_tickets:
				tickets = Ticket.objects.filter(created_user_id=request.user.id).order_by('-ticket_id')
				ticket_detail = TicketDetail.objects.filter(created_user_id=request.user.id)
			else:
				return render(request,self.template_name,{'property':self.form1})

		else:
			is_tickets=Ticket.objects.all()
			if  is_tickets:
				tickets = Ticket.objects.all().order_by('-ticket_id')
				ticket_detail = TicketDetail.objects.all()
			else:
				return render(request,self.template_name,{'property':self.form1})

		ticket_list=[]
		for ticket in tickets:
			ticket_dict={}
			if(User.objects.filter(id=ticket.created_user_id).exists()):
				obj_user = User.objects.get(id=ticket.created_user_id)
				ticket_dict['user_name'] = obj_user.first_name.capitalize() + ' ' + obj_user.last_name.capitalize()
			else:
				pass
			 
			ticket_dict['user_name'] = obj_user.first_name.capitalize() + ' ' + obj_user.last_name.capitalize()
			ticket_dict['title'] = ticket.title
			ticket_dict['ticket_id'] = ticket.ticket_id
			ticket_dict['type'] = ticket.type
			ticket_dict['created_date_time'] = ticket.created_date_time
			ticket_dict['status'] = ticket.status
			ticket_dict['priority'] = ticket.priority
 			ticket_list.append(ticket_dict)
		
		
		return render(request,self.template_name,{'tickets':tickets,'details':ticket_detail,'ticket_list':ticket_list,'property':self.form1})
			

	def post(self,request,*args,**kwargs):
		form = self.form1(request.POST)
		if form.is_valid():
			form_data =form.cleaned_data
			if not request.user.is_staff:
				is_tickets=Ticket.objects.filter(created_user_id=request.user.id).exists()
				if  is_tickets:
					tickets = Ticket.objects.filter(created_user_id=request.user.id).order_by('-ticket_id')
					ticket_detail = TicketDetail.objects.filter(created_user_id=request.user.id)

					status = form_data['status']
					priority = form_data['priority']
					type = form_data['type']
					date_from = form_data['start_date'] 
					date_to = form_data['end_date']

					statusobj = TicketStatus.objects.filter(status_name=status)
					priorityobj = TicketPriority.objects.filter(priority_name=priority)
					typeobj = TicketType.objects.filter(type_name=type)

					tickets = Ticket.objects.filter(created_user_id=request.user.id) #,status=statusobj,type=typeobj,priority=priorityobj)
					if statusobj:
						tickets = tickets.filter(status=statusobj)
					if typeobj:
						tickets = tickets.filter(type=typeobj)
					if priorityobj:
						tickets = tickets.filter(priority=priorityobj)
					if date_from:
						tickets = tickets.filter(created_date_time__gt = datetime.strptime(str(date_from), '%Y-%m-%d'))
						#tickets = tickets.filter(created_date_time__gt = '2017-01-06')
					if date_to:
						tickets = tickets.filter(created_date_time__lt = datetime.strptime(str(date_to), '%Y-%m-%d'))


					ticket_detail = TicketDetail.objects.all()
					if tickets:
						ticket_list=[]
						for ticket in tickets:
							ticket_dict={}
							if(User.objects.filter(id=ticket.created_user_id).exists()):
								obj_user = User.objects.get(id=ticket.created_user_id)
								ticket_dict['user_name'] = obj_user.first_name.capitalize() + ' ' + obj_user.last_name.capitalize()
							else:
								pass
							 
							try:
								ticket_dict['user_name'] = obj_user.first_name.capitalize() + ' ' + obj_user.last_name.capitalize()
							except:
								ticket_dict['user_name']='' 
							ticket_dict['title'] = ticket.title
							ticket_dict['ticket_id'] = ticket.ticket_id
							ticket_dict['type'] = ticket.type
							ticket_dict['created_date_time'] = ticket.created_date_time
							ticket_dict['status'] = ticket.status
							ticket_dict['priority'] = ticket.priority
				 			ticket_list.append(ticket_dict)

						return render(request,self.template_name,{'tickets':tickets,'details':ticket_detail,'ticket_list':ticket_list,'property':form})
				else:
					#no tickets to show
					return render(request,self.template_name,{'property':self.form})

			else:
				is_tickets=Ticket.objects.filter(deleted=False).exists()
				if  is_tickets:
					tickets = Ticket.objects.filter(deleted=False).order_by('-ticket_id')
					ticket_detail = TicketDetail.objects.all()

					status = form_data['status']
					priority = form_data['priority']
					type = form_data['type']
					date_from = form_data['start_date'] 
					date_to = form_data['end_date']

					statusobj = TicketStatus.objects.filter(status_name=status)
					priorityobj = TicketPriority.objects.filter(priority_name=priority)
					typeobj = TicketType.objects.filter(type_name=type)

					tickets = Ticket.objects.filter(deleted=False) #,status=statusobj,type=typeobj,priority=priorityobj)
					if statusobj:
						tickets = tickets.filter(status=statusobj)
					if typeobj:
						tickets = tickets.filter(type=typeobj)
					if priorityobj:
						tickets = tickets.filter(priority=priorityobj)
					if date_from:
						tickets = tickets.filter(created_date_time__gt = datetime.strptime(str(date_from), '%Y-%m-%d'))
						#tickets = tickets.filter(created_date_time__gt = '2017-01-06')
					if date_to:
						tickets = tickets.filter(created_date_time__lt = datetime.strptime(str(date_to), '%Y-%m-%d'))


					ticket_detail = TicketDetail.objects.all()
				if tickets:
					ticket_list=[]
					for ticket in tickets:
						ticket_dict={}
						if(User.objects.filter(id=ticket.created_user_id).exists()):
							obj_user = User.objects.get(id=ticket.created_user_id)
							ticket_dict['user_name'] = obj_user.first_name.capitalize() + ' ' + obj_user.last_name.capitalize()
						else:
							pass
						 
						try:
							ticket_dict['user_name'] = obj_user.first_name.capitalize() + ' ' + obj_user.last_name.capitalize()
						except:
							ticket_dict['user_name']=''
						ticket_dict['title'] = ticket.title
						ticket_dict['ticket_id'] = ticket.ticket_id
						ticket_dict['type'] = ticket.type
						ticket_dict['created_date_time'] = ticket.created_date_time
						ticket_dict['status'] = ticket.status
						ticket_dict['priority'] = ticket.priority
			 			ticket_list.append(ticket_dict)

				else:
					#no tickets to show
					return render(request,self.template_name,{'property':form})
				
				return render(request,self.template_name,{'tickets':tickets,'details':ticket_detail,'ticket_list':ticket_list,'property':form})
			
			#
			#return render(request,self.template_name,{'tickets':tickets,'details':ticket_detail,'ticket_list':ticket_list,'property':self.form1})

		#if form not valid
		return render(request,self.template_name,{'tickets':tickets,'details':ticket_detail,'property':form})

			

"""-----------AJAX----------"""

def check_email(request):
	"""AJAX for checking email"""
	email_id = str(request.GET['id'])
	user = User.objects.filter(username=email_id,is_active=1).exists()
	if user:
		return HttpResponse(1)
	else:
		return HttpResponse(0)


@login_required()
def home(request):
	return render(request,"home.html")

# def home(request):
# 	context = RequestContext(request,{'request': request,'user': request.user})
# 	return render_to_response('home.html',context_instance=context)

@login_required()
def profile(request):
	return render(request,"profile.html")

@login_required()
def tickets(request):
	form1 = TicketListForm()
	if request.method == 'GET':
		if not request.user.is_staff:
			 
			is_tickets=Ticket.objects.filter(created_user_id=request.user.id, deleted=False).exists()
			if  is_tickets:
				ticket = Ticket.objects.filter(created_user_id=request.user.id, deleted=False).order_by('-ticket_id')
				ticket_detail = TicketDetail.objects.filter(created_user_id=request.user.id)
				ticket = ticket_formating(ticket)
				return render(request,"tickets.html",{'tickets':ticket,'details':ticket_detail})
			else:
				return render(request,"tickets.html")
		else:
			
			
			is_tickets=Ticket.objects.filter(deleted=False).exists()
			if  is_tickets:
				ticket = Ticket.objects.filter(deleted=False).order_by('-ticket_id')
				ticket_detail = TicketDetail.objects.all()

				ticket = ticket_formating(ticket)

				return render(request,"tickets.html",{'tickets':ticket,'details':ticket_detail,'form1':form1})
			else:
				return render(request,"tickets.html")

	elif request.method == 'POST':

		form2 = TicketListForm(request.POST)
		if form2.is_valid():
			form_data = form2.cleaned_data
			email = form_data['user']
			status = form_data['status']
			statusobj = TicketStatus.objects.filter(status_name=status)
			is_tickets=Ticket.objects.filter(deleted=False).exists()
			if  is_tickets:
				ticket = Ticket.objects.filter(deleted=False).order_by('-ticket_id')
				if email :
					user = User.objects.get(username = email)
					ticket = ticket.filter(created_user_id=user.id).order_by('-ticket_id')
				if statusobj:
					ticket = ticket.filter(status=statusobj).order_by('-ticket_id')

				ticket_detail = TicketDetail.objects.all()

				ticket = ticket_formating(ticket)

				return render(request,"tickets.html",{'tickets':ticket,'details':ticket_detail,'form1':form2})
			else:
				return render(request,"tickets.html",{'form1':form2})
		else:
			return render(request,"tickets.html",{'tickets':ticket,'details':ticket_detail,'form1':form2})








"""@login_required()
def edit(request):
	return render(request,"ticket_edit.html")"""

@login_required()
def delete(request,pk):
	is_ticket = Ticket.objects.filter(ticket_id=pk,created_user_id=request.user.id).exists()
	if is_ticket:
		ticket = Ticket.objects.get(ticket_id=pk,created_user_id=request.user.id)
		ticket.deleted = True
		ticket.save()
		return HttpResponseRedirect(reverse('tickets'))
	return HttpResponseRedirect(reverse('tickets'))



	









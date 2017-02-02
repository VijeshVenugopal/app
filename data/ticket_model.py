"""Ticket_Model"""
from django.db import models
from datetime import datetime 
import uuid

class TicketStatus(models.Model):
	"""class moddel for ticket status"""
	status_id = models.AutoField(primary_key=True)
	status_name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	deleted = models.BooleanField()

	def __unicode__(self):
		return self.status_name

class TicketPriority(models.Model):
	"""class moddel for Ticket priority"""
	priority_id = models.AutoField(primary_key=True)
	priority_name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	deleted = models.BooleanField(default=False)

	def __unicode__(self):
		return self.priority_name

class TicketType(models.Model):
	"""class moddel for ticket types"""
	type_id = models.AutoField(primary_key=True)
	type_name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	deleted = models.BooleanField(default=False)

	def __unicode__(self):
		return self.type_name

class Ticket(models.Model):
	"""class moddel for ticket"""
	ticket_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=250)
	status = models.ForeignKey(TicketStatus)
	priority = models.ForeignKey(TicketPriority)
	type = models.ForeignKey(TicketType)
	assigned_user_id = models.IntegerField()
	created_user_id = models.IntegerField()
	created_date_time = models.DateTimeField(default=datetime.now())
	deleted = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title

class TicketDetail(models.Model):
	"""class moddel for ticket details"""
	ticket_detail_id = models.AutoField(primary_key=True)
	ticket = models.ForeignKey(Ticket)
	ticket_text = models.TextField()
	status = models.ForeignKey(TicketStatus)
	created_user_id = models.IntegerField()
	created_date_time = models.DateTimeField(default=datetime.now())

	def __unicode__(self):
		return self.ticket_text

class TicketAttachment(models.Model):
	"""class moddel for ticket attachments"""
	ticket_attachment_id = models.AutoField(primary_key=True)
	ticket = models.ForeignKey(Ticket)
	ticket_detail = models.ForeignKey(TicketDetail)
	original_file_name = models.CharField(max_length=200)
	file_name = models.CharField(max_length=500)
	created_user_id = models.IntegerField()
	created_date_time = models.DateTimeField(default=datetime.now())
	deleted = models.BooleanField(default=False)

	def __unicode__(self):
		return self.original_file_name

class ResetPassword(models.Model):
	reset_password_id = models.AutoField(primary_key=True)
	reset_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	#created_user_id = models.IntegerField()
	email = models.EmailField()
	created_date_time = models.DateTimeField(default=datetime.now())
	deleted = models.BooleanField(default=False)

	def __unicode__(self):
		result = str(self.reset_code) + " for " + str(self.email) + ". Deleted: "+ str(self.deleted)
		return result





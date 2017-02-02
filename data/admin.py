from django.contrib import admin

# Register your models here.

from data.models import *

admin.site.register(Ticket)
admin.site.register(TicketDetail)
admin.site.register(TicketAttachment)
admin.site.register(ResetPassword)
admin.site.register(TicketStatus)
admin.site.register(TicketType)
admin.site.register(TicketPriority)

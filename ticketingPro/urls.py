"""ticketingPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$', tickets, name='tickets'),
	#url(r'^googleda01d44f8d16bea3.html/$', google, name='google'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'', include('social.apps.django_app.urls', namespace='social')),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^signup/$', SignupView.as_view(), name='signup'),
	#url(r'^home/$', home, name='home'),
	url(r'^report/$', ReportView.as_view(), name='report'),
	url(r'^profile/$',profile,name='profile'),
	url(r'^tickets/create$',CreateTicket.as_view(),name='tickets_create'),
	url(r'^tickets/edit/(?P<pk>[0-9]+)/$',EditTicket.as_view(),name='edit'),
	url(r'^tickets/delete/(?P<pk>[0-9]+)/$',delete,name='delete'),
	url(r'^tickets/$',tickets,name='tickets'),
	url(r'^ajax_check_email/$', check_email, name='check_email'),
	url(r'^forgotpassword/$', ForgotPassword.as_view(), name='forgotpassword'),
	url(r'^forgotpassword/reset/(?P<uuid>[^/]+)/$', ResetPasswordView.as_view(), name='reset'),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

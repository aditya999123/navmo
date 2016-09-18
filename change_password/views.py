from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from register.models import user_data
import requests
from change_password.models import password_reset_otp

# Create your views here.
def change_password(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/home")
	else:
		if(request.method=="GET"):
			reference_id=request.GET.get('reference_id')
			
			print reference_id
			login_display='<li><a href="/register">Register</a></li>'
			login_display2='<li><a href="/login">Login</a></li>'
			return render(request,'change_password/change_password.html',{"login_display":login_display,"login_display2":login_display2,"reference_id":reference_id})
		else:


			otp_data=password_reset_otp.objects.get(refrence_id=request.GET.get('reference_id'))
			setattr(otp_data,'flag',1)
			login_display='<li><a href="/register">Register</a></li>'
			login_display2='<li><a href="/login">Login</a></li>'
			
			print requests.request('GET', url)		
			return HttpResponseRedirect('/',{"login_display":login_display,"login_display2":login_display2})
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from register.models import user_data
import requests
from random import randint
from change_password.models import password_reset_otp

# Create your views here.
def forgot_password(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/home")
	else:
		if(request.method=="GET"):
			login_display='<li><a href="/register">Register</a></li>'
			login_display2='<li><a href="/login">Login</a></li>'
			return render(request,'forgot_password/forgot_password.html',{"login_display":login_display,"login_display2":login_display2})
		else:

			otp=randint(99999,999999)
			try:
				password_reset_otp.objects.Create(reference_id,user_data_all.number,otp,0)
			except Exception, e:
				#Do nothing
			else:
				setattr(password_reset_otp.objects.get(reference_id),'otp',otp)
				setattr(password_reset_otp.objects.get(reference_id),'flag',0)
			

			user_data_all=user_data.objects.get(refrence_id=request.POST.get('reference_id'))
			url='http://api.msg91.com/api/sendhttp.php?authkey=125195AvX4LUlVf57dcd941&mobiles='
			url+=user_data_all.number

			#url+='&message='+'E-Cell team welcomes you. \nVerification code for the app is '+otp
			url+='&message= Hello '+user_data_all.first_name+' Your otp for password reset is '+otp+' and reference id is '+request.POST.get('reference_id')
			url+='.'+'&sender=mNavmo&route=4'
			login_display='<li><a href="/register">Register</a></li>'
			login_display2='<li><a href="/login">Login</a></li>'
		#	print requests.request('GET', url)

			return HttpResponseRedirect('/change_password/?reference_id'+request.POST.get('reference_id'),{"login_display":login_display,"login_display2":login_display2})
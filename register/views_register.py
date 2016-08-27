from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
@csrf_protect
def registration(request):
	if request.user.is_authenticated():
		return render(request,'register/logoutandregister.html')
	else:
		return render(request,'register/register.html')
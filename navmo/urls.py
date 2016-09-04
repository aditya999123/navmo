"""navmo URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from register.views_register import registration,home,login_check,logout_page
from register.views_register import logout_and_register
from otp.views import verify_mobile,test
from payment.views import payment
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^accounts/login/$', login_check),
    url(r'^register/$',registration ),
    url(r'^home/$',home ),
    url(r'^logout/$',logout_page ),
    url(r'^logout_and_register/$',logout_and_register),
    url(r'^payment/$',payment ),
    url(r'^verify_mobile/$',verify_mobile ),
    url(r'^test/$',test),

]

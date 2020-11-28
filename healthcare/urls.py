"""healthcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('login/',userLogin,name='login'),
    path('logout/',userLogout,name='logout'),
    path('createAccount/',createAccount,name='createaccount'),
    path('adminLogin/',adminLogin,name='adminlogin'),
    path('contact/',contactUs,name='contact'),
    path('home/',dashboard,name='p_home'),
    path('profile/', profile, name='profile'),
    path('makeAppointment/', MakeAppointments, name='makeappoint'),
    path('viewAppointment/', ViewAppointments, name='viewappoint'),

]

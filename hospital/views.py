from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
import time
from django.utils import timezone
# Create your views here.


def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'header.html')

def userLogin(request):
    if request.method=='POST':
        email_id=request.POST['email']
        print(email_id)
        pswd=request.POST['pass']
        user=authenticate(request,username=email_id,password=pswd)
        try:
            error = ""
            page = ""
            if user is not None:
                login(request, user)
                error = "no"
                g = request.user.groups.all()[0].name
                if g == 'Doctor':
                    page = "doctor"
                    d = {'error': error, 'page': page}
                    return render(request, 'doctorhome.html', d)
                elif g == 'Patient':
                    page = "patient"
                    d = {'error': error, 'page': page}
                    return render(request, 'patienthome.html', d)
            else:
                error = "yes"
        except Exception as e:
            error = "yes"
        # print(e)

    return render(request,'login.html')

def createAccount(request):
    error=""
    user= "none"
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        email = request.POST['email']
        password = request.POST['pass']
        repeatpassword = request.POST['repeatPass']
        address = request.POST['address']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        bloodGroup = request.POST['bloodGroup']
        birthdate = request.POST['DOB']

        try:
            if password == repeatpassword:
                Patient.objects.create(patient_name=patient_name, email=email, address=address,
                                       mobile=mobile, gender=gender, DOB=birthdate, bloodGroup=bloodGroup)
                user = User.objects.create_user(first_name=patient_name, email=email, password=password, username=email)
                patientGroup = Group.objects.get(name='Patient')
                patientGroup.user_set.add(user)
                user.save()
                error="no error"
            else:
                error="yes there is error"

        except Exception as e:
            error = "yes there is error"
            print(e)

    params={'error':error}
    return render(request,'createAccount.html',params)


def userLogout(request):
    logout(request)
    return redirect('login')


def adminLogin(request):
    return render(request,'aboutUS.html')

def contactUs(request):
    return render(request,'aboutUS.html')


def dashboard(request):
    if not request.user.is_active:
        return redirect('login')

    g = request.user.groups.all()[0].name
    if g == 'Doctor':
        return render(request, 'doctorhome.html')

    elif g == 'Patient':
        return render(request, 'patienthome.html')



def profile(request):
    if not request.user.is_active:
        return redirect('login')

    g = request.user.groups.all()[0].name
    if g == 'Patient':
        patient_details = Patient.objects.all().filter(email=request.user)

        d = {'patient_details': patient_details}
        print(d)
        return render(request, 'profile_patient.html', d)


def MakeAppointments(request):
    error = ""
    if not request.user.is_active:
        return redirect('login')
    alldoctors = Doctor.objects.all()
    d = {'alldoctors': alldoctors}
    g = request.user.groups.all()[0].name
    if g == 'Patient':
        if request.method == 'POST':

            doctoremail = request.POST['doctoremail']
            doctorname = request.POST['doctorname']
            patientname = request.POST['patientname']
            patientemail = request.POST['patientemail']
            appointmentdate = request.POST['appointmentdate']
            appointmenttime = request.POST['appointmenttime']
            symptoms = request.POST['symptoms']
            try:
                Appointment.objects.create(patient_name=patientname, doctor_name=doctorname, p_email=patientemail,
                                          d_email=doctoremail,appoint_date=appointmentdate, appoint_time=appointmenttime, symptoms=symptoms,
                                          prescription="",status=True)
                error = "no"
            except Exception as e:
                print("err is ",e)
                error = "yes"
            e = {"error": error}
            return render(request, 'patientmakeappointment.html', e)
        elif request.method == 'GET':
            return render(request, 'patientmakeappointment.html', d)



def ViewAppointments(request):
    if not request.user.is_active:
        return redirect('login')
    g = request.user.groups.all()[0].name
    if g == 'Patient':
        upcoming_appointments = Appointment.objects.filter(p_email=request.user,
                                                           appoint_date__gte=timezone.now(), status=True).order_by('appoint_date')
        # print("Upcomming Appointment",upcomming_appointments)
        previous_appointments = Appointment.objects.filter(p_email=request.user,
                                                           appoint_date__lt=timezone.now()).order_by('-appoint_date') | Appointment.objects.filter(p_email=request.user, status=False).order_by(
            '-appoint_date')
        # print("Previous Appointment",previous_appointments)
        d = {"upcoming_appointments": upcoming_appointments, "previous_appointments": previous_appointments}
        return render(request, 'patient_view_appoints.html', d)


from django.shortcuts import render
from .models import RegistrationData
from .forms import LoginForm,RegistrationForm
from django.http.response import HttpResponse

def loginview(request):
    if request.method == 'POST':
        lform = LoginForm(request.POST)
        if lform.is_valid():
            user1 = request.POST.get('username')
            password1 = request.POST.get('password')
            login = RegistrationData.objects.filter(username=user1,password=password1)
            if login:
                return HttpResponse("Login Sucess")
            else:
                return HttpResponse("Login Failed")
        else:
            return HttpResponse('Invalid User')
    else:
        lform = LoginForm()
        return render(request,'login.html',{'lform':lform})
def registrationview(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            loc = request.POST.get('location')
            user = request.POST.get('username')
            pwd = request.POST.get('password')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            data = RegistrationData(first_name=fname,last_name=lname,location=loc,username=user,
                                    password=pwd,email=email,mobile=mobile)
            data.save()
            lform = LoginForm()
            return render(request,'login.html',{'lform':lform})
        else:
            return HttpResponse("Invalid User Data")

    else:
        rform = RegistrationForm()
        return render(request,"registration.html",{'rform':rform})
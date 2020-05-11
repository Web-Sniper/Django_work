from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import pyplot
from .models import EnquiryData

def index(request):
    return render(request,'index.html')

def enquiry(request):
    if request=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')
        query = request.cleaned_data('query')
        data = EnquiryData(
            name = name,
            email = email,
            city = city,
            mobile = mobile,
            query = query,

            )
        data.save()
    return render(request,'enquiry.html')

def crop_evaluation(request):
    return


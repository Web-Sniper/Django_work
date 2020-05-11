from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import pyplot
from .forms import EnquiryForm
from .models import EnquiryData

def index(request):
    return render(request,'index.html')

def enquiry(request):
    if request=='POST':
        eform = EnquiryForm(request.POST)
        if eform.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            city = request.POST.get('city')
            mobile = request.POST.get('mobile')
            query = request.POST.get('query')
            data = EnquiryData(
                name = name,
                email = email,
                city = city,
                mobile = mobile,
                query = query,

            )
            data.save()
            eform = EnquiryForm()
            return render(request,'enquiry.html',{'eform':eform})
        else:
            return HttpResponse("Invalid User Data")
    else:
        eform = EnquiryForm()
        return render(request, 'enquiry.html', {'eform': eform})

def crop_evaluation(request):
    return


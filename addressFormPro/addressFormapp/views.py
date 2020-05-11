from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Address
from .forms import AddrForm

def addrview(request):
    if request.method=='POST':
        aform = AddrForm(request.POST)
        if aform.is_valid():
            name1 = request.POST.get('name')
            mobile1 = request.POST.get('mobile')
            city1 = request.POST.get('city')
            address1 = request.POST.get('address')
            a = Address(name=name1,mobile=mobile1,city=city1,address=address1)
            a.save()
            aform = AddrForm()
            return render(request,'address.html',{'aform':aform})
        else:
            return HttpResponse('Invalid data')
    else:
        aform = AddrForm()
        return render(request,'address.html',{'aform':aform})
def displaydata(request):
    data = Address.objects.all()
    return render(request,'details.html',{'data':data})


from django.shortcuts import render
from .models import InputFrm
from django.http import HttpResponse
def enter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        data = InputFrm(
            name=name
        )

        data.save()
        return HttpResponse("Data Inserted")
    else:
        return render(request, 'index.html')
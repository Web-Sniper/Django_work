from django.shortcuts import render
from django.http.response import HttpResponse
import datetime as dt

date1 = dt.datetime.now()

def home(request):
    x = "<h1>Welcome to django home...</h1>"
    return HttpResponse(x)
def contact(request):
    y = "<h2>My contact is 8127670821</h2>"
    return HttpResponse(y)
def feedback(request):
    z = "Feedback is good"
    return HttpResponse(z)
def date(request):
    return HttpResponse(date1)

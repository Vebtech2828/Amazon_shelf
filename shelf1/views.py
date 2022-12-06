from django.shortcuts import render
from django.http import HttpResponse
import datetime
def headline(request):
    return HttpResponse('<h1>Amazon Warehouse</h1>')
def current_time(request):
    time = datetime.datetime.now()
    ti = '<h1>Your Visit time is :'+str(time)+'</h1>'
    return HttpResponse(ti)

def wish(request):
    return render(request, 'shelf1/result.html')

from django.shortcuts import render

from django.http import HttpResponse

def first_view(request):
    return HttpResponse('<h1>Response from First View</h1>')
def second_view(request):
    return HttpResponse('<h1>Response from Second View</h1>')
def third_view(request):
    return HttpResponse('<h1>Response from third View</h1>')
def fourth_view(request):
    return HttpResponse('<h1>Response from Fourth View</h1>')
def fifth_view(request):
    return HttpResponse('<h1>Response from Fifth View</h1>')

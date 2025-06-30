from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pay_dj(request):
    return HttpResponse('5000')
def pay_python(request):
    return HttpResponse('10000')
def pay_fsd(request):
    return HttpResponse('6400')
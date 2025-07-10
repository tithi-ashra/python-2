from django.shortcuts import render
from app1.models import student
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home of Student')
def roll(request):
    stu = student.objects.all()
    return render(request,'i2.html',{"students":stu})
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_dj(request):
    return HttpResponse('Hello django')
def learn_python(request):
    return HttpResponse('Hello Python')
def learn_fsd(request):
    return HttpResponse('Hello fsd')

def learn_html(request):
    return render(request,'course1.html')
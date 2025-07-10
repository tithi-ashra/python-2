from django.shortcuts import render,redirect
from roll.models import Student

# Create your views here.
def home(request):
    data = Student.objects.all()
    return render(request, 'home.html', {'roll': data})
def welcome(request):
    return render(request,'welcome.html')
def student_search(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        if query:
            data = Student.objects.filter(Name__icontains=query)
        else:
            data = Student.objects.all()
        return render(request, 'home.html', {'roll': data})
    else:
        # For GET request, redirect to home or show all students
        return redirect('home')
def stuinformation(request,id):
    pi = Student.objects.get(pk=id)
    return render(request,'inform.html',{'roll':pi})
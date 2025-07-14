from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from students.models import Student

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{"form":form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{"form":form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()
    return render(request,'list.html',{'student':students})

@login_required(login_url='login')
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['mail']
        roll = request.POST['roll']
        birthdate = request.POST['birthdate']
        subject1 = request.POST['sub']
        thgrade = request.POST['thg']
        prgrade = request.POST['prg']
        Student.objects.create(name=name,roll=roll,email=email,birthdate=birthdate,subject1=subject1,thgrade=thgrade,prgrade=prgrade)
        return redirect('student_list')
    return render(request,'add.html')

@login_required(login_url='login')
def edit_student(request,id):
    student = get_object_or_404(Student,pk=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['mail']
        student.roll = request.POST['roll']
        student.birthdate = request.POST['birthdate']
        student.subject1 = request.POST['sub']
        student.thgrade = request.POST['thg']
        student.prgrade = request.POST['prg']
        student.save()
        return redirect('student_list')
    return render(request,'edit.html',{'student':student})

def delete_student(request,id):
    student = get_object_or_404(Student,pk=id)
    student.delete()
    return redirect('student_list')
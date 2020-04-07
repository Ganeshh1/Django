from django.shortcuts import render,redirect
from Records.models import Student,School,Subject_Name
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
def home(request):
    context={'Students':Student.objects.all()}
    return render(request,'Records/home.html',{'Students':Student.objects.all()})

def display(request):
    reg_no=int(request.GET['Value'])
   
    student=Student.objects.get(reg_no=reg_no)
    
    
    context={
        'Student':Student.objects.get(reg_no=reg_no),
        'Subjects':Subject_Name.objects.filter(student_name=student),

    }
    return render(request,'Records/Student_display.html',context)
def Create(request):
    context={'Students':Student.objects.all(),'School':School.objects.all(),'Sub_name':Subject_Name.objects.all()}
    return render(request,'Records/Student_create.html',context)
def Create_New_student(request):
    name=request.GET['name']
    phone_number=int(request.GET['phone_no'])
    reg_no=request.GET['reg_no']
    school_name=request.GET['school_name']
    phone_no=request.GET['school_no']
    school_location=request.GET['school_location']
    school=School(school_name=school_name,phone_no=phone_no,school_location=school_location)
    school.save()
    student=Student(name=name,reg_no=reg_no,phone_no=phone_number)
    student.save()
    return render(request,'Records/Student_details.html',{'Students':Student.objects.all()})
def Create_school(request):
    return render(request,'Records/Create_school.html')
def Create_student(request):
    return render(request,'Records/Create_student.html')    
def Create_subject(request):
    
    return render(request,'Records/Create_subject.html',{'Students':Student.objects.all()})    

def Create_New_school(request):
    school_name=request.GET['school_name']
    school_number=int(request.GET['school_no'])
    school_location=request.GET['school_location']
    school=School(school_name=school_name,phone_no=school_number,school_location=school_location)
    school.save()
    return render(request,'Records/Student_details.html',{'Students':Student.objects.all()})

def Create_New_subject(request):
    sub_name=request.GET['sub_name']
    sub_mark=request.GET['sub_mark']
    student_name=request.GET['Value']
    student=Student.objects.get(name=student_name)
    subject=Subject_Name(sub_name=sub_name,mark=sub_mark,student_name=student)
    subject.save()
    return render(request,'Records/Student_details.html',{'Students':Student.objects.all()})

def Register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Your Account has been created ! You can Log-In')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'Records/Register.html',{'form':form})

@login_required
def Profile(request):
    return render(request,'Records/profile.html')

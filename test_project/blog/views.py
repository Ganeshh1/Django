from django.shortcuts import render
from .models import Post,Post1,StudentDetails,Student


# from django.http import HttpResponse

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)
def about(request):
    context={
        'Student':Student.objects.all()
    }

    return render(request,'blog/about.html',context)

def display(request):
    return render(request,'blog/Validation.html')

def Print(request):
    val=int(request.GET['Value'])
   
    a=StudentDetails.objects.all()
    context={
        'Student':StudentDetails.objects.all()[int(val)]
    }
    return render(request,'blog/Students.html',context)



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
    context={
        'Student':StudentDetails.objects.all()[0]
    }
    return render(request,'blog/Students.html',context)



from django.shortcuts import render
from .models import Post,Post1


# from django.http import HttpResponse

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)
def about(request):
    context={
        'posts':Post1.objects.all()
    }

    return render(request,'blog/about.html',context)





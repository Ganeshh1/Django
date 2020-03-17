from django.shortcuts import render
from blog.models import StudentDetails

def display(request):
    return render(request,'Student/Student_details.html')

def Print(request):
    val=int(request.GET['Value'])
   
    a=StudentDetails.objects.all()
    context={
        'Student':StudentDetails.objects.all()[int(val)]
    }
    return render(request,'Student/Student_display.html',context)



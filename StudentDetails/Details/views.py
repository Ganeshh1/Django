from django.shortcuts import render
from Details.models import StudentDetails,School,Sub_name


def display(request):
    context={'Students':StudentDetails.objects.all()}
    return render(request,'StudentDetails/Student_details.html',{'Students':StudentDetails.objects.all()})

def Print(request):
    reg_no=int(request.GET['Value'])
   
    a=StudentDetails.objects.all()
    context={
        'Student':StudentDetails.objects.get(reg_no=reg_no)
    }
    return render(request,'StudentDetails/Student_display.html',context)
def Create(request):
    context={'Students':StudentDetails.objects.all(),'School':School.objects.all(),'Sub_name':Sub_name.objects.all()}
    return render(request,'StudentDetails/Student_create.html',context)
def Create_New_student(request):
    name=request.GET['name']
    phone_number=int(request.GET['phone_no'])
    reg_no=request.GET['reg_no']
    school_name=request.GET['school_name']
    school_no=request.GET['school_no']
    school_location=request.GET['school_location']
    a=School(school_name=school_name,school_no=school_no,school_location=school_location)
    a.save()
    Sub_1=[request.GET['Sub_1'],request.GET['Sub_1-name']]
    Sub_2=[request.GET['Sub_2'],request.GET['Sub_2-name']]
    Sub_3=[request.GET['Sub_3'],request.GET['Sub_3-name']]
    Sub_4=[request.GET['Sub_4'],request.GET['Sub_4-name']]
    b=Sub_name(name=Sub_1[1],mark=Sub_1[0])
    c=Sub_name(name=Sub_2[1],mark=Sub_2[0])
    d=Sub_name(name=Sub_3[1],mark=Sub_3[0])
    e=Sub_name(name=Sub_4[1],mark=Sub_4[0])
    b.save()
    c.save()
    e.save()
    d.save()
    z=StudentDetails(name=name,reg_no=reg_no,phone_no=phone_number,school=a,Sub_1=b,Sub_2=c,Sub_3=d,Sub_4=e)
    z.save()
    return render(request,'StudentDetails/Student_details.html',{'Students':StudentDetails.objects.all()})
def Create_school(request):
    return render(request,'StudentDetails/Create_school.html')
def Create_student(request):
    return render(request,'StudentDetails/Create_student.html')    
def Create_New_school(request):
    school_name=request.GET['school_name']
    school_number=int(request.GET['school_no'])
    school_location=request.GET['school_location']
    z=School(school_name=school_name,school_no=school_number,school_location=school_location)
    z.save()
    return render(request,'StudentDetails/Student_details.html',{'Students':StudentDetails.objects.all()})
def Create_New_subject(request):
    sub_name=request.GET['sub_name']
    sub_mark=request.GET['sub_mark']
    z=Sub_name(name=sub_name,mark=sub_mark)
    z.save()
    return render(request,'StudentDetails/Student_details.html',{'Students':StudentDetails.objects.all()})

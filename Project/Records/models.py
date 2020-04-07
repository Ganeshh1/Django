from django.db import models



class School(models.Model):
    school_name=models.CharField(max_length=100)
    phone_no=models.IntegerField()  
    school_location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.school_name


class Student(models.Model):
    name=models.CharField(max_length=100)
    reg_no=models.BigIntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    phone_no=models.IntegerField()
    
    def __str__(self):
        return self.name

class Subject_Name(models.Model):
    sub_name=models.CharField(max_length=50)
    mark=models.IntegerField()
    student_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        return self.sub_name

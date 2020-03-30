from django.db import models



class School(models.Model):
    school_name=models.CharField(max_length=100)
    school_no=models.IntegerField()  
    school_location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.school_name
class Sub_name(models.Model):
    name=models.CharField(max_length=50)
    mark=models.IntegerField()

    def __str__(self):
        return self.name


class StudentDetails(models.Model):
    name=models.CharField(max_length=100)
    reg_no=models.BigIntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    phone_no=models.IntegerField()
    
    Sub_1=models.ForeignKey(Sub_name,on_delete=models.CASCADE,related_name='Subject_one')
    Sub_2=models.ForeignKey(Sub_name,on_delete=models.CASCADE,related_name='Subject_2')
    Sub_3=models.ForeignKey(Sub_name,on_delete=models.CASCADE,related_name='Subject_3')
    Sub_4=models.ForeignKey(Sub_name,on_delete=models.CASCADE,related_name='Subject_4')

    def __str__(self):
        return self.name
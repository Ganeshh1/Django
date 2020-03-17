from django.db import models

class Maths_mark(models.Model):
    mark=models.IntegerField()
class Social_mark(models.Model):
    mark=models.IntegerField()
class English_mark(models.Model):
    mark=models.IntegerField()
class Science_mark(models.Model):
    mark=models.IntegerField()
class Subjects_name(models.Model):
   math=models.ForeignKey(Maths_mark,on_delete=models.CASCADE)
   science=models.ForeignKey(Social_mark,on_delete=models.CASCADE)
   social=models.ForeignKey(Science_mark,on_delete=models.CASCADE)
   english=models.ForeignKey(English_mark,on_delete=models.CASCADE)


class School(models.Model):
    school_name=models.CharField(max_length=100)
    school_no=models.IntegerField()
    school_location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.school_name



class StudentDetails(models.Model):
    name=models.CharField(max_length=100)
    reg_no=models.BigIntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    phone_no=models.IntegerField()
    Sub_mark=models.ForeignKey(Subjects_name,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

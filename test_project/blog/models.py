from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post1(models.Model):
    name=models.CharField(max_length=100)
    age=models.TextField()

    

    def __str__(self):
        return self.name
    
class Post2(models.Model):
    name=models.CharField(max_length=100)
    URL=models.URLField()

    def __str__(self):
        return 'URLField_Post'

class Post3(models.Model):
    name=models.CharField(max_length=100)
    age=models.BigIntegerField()

    def __str__(self):
        return 'BigIntegerField_Post'

class Post4(models.Model):
    name=models.CharField(max_length=100)
    Enter_a_binary_number=models.BinaryField()

    def __str__(self):
        return 'BinaryField_Post'


class Post5(models.Model):
    name=models.CharField(max_length=100)
    Enter_true_or_false=models.BooleanField()

    def __str__(self):
        return 'BooleanField_Post'

    

class Post6(models.Model):
    name=models.CharField(max_length=100)
    Decimal=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return 'DecimalField_Post'


class Post7(models.Model):
    name=models.CharField(max_length=100)
    Email=models.EmailField()

    def __str__(self):
        return 'EmailField_Post'


class Post8(models.Model):
    name=models.CharField(max_length=100)
    Floatnumber=models.FloatField()

    def __str__(self):
        return 'FloatField_Post'


class Post9(models.Model):
    name=models.CharField(max_length=100)
    Ip=models.GenericIPAddressField()

    def __str__(self):
        return 'GenericIPAddressField_Post'


class Post10(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return 'IntegerField_Post'

class Post11(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return 'IntegerField_Post'

class Post12(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return 'IntegerField_Post'

class Post13(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return 'IntegerField_Post'

class Post14(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField()

    def __str__(self):
        return 'DateTimeField_Post'

class Post15(models.Model):
    name=models.CharField(max_length=100)
    Floatnumber=models.FloatField()

    def __str__(self):
        return 'FloatField_Post'

class Post16(models.Model):
    name=models.CharField(max_length=100)
    Floatnumber=models.FloatField()

    def __str__(self):
        return 'FloatField_Post'

class Post17(models.Model):
    name=models.CharField(max_length=100)
    Floatnumber=models.FloatField()

    def __str__(self):
        return 'FloatField_Post'



from django.contrib import admin


# Register your models here.
from .models import Student,School,Subject_Name

admin.register(Student,School,Subject_Name)(admin.ModelAdmin)
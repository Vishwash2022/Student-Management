from django.db import models

class User(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Password=models.CharField(max_length=500,blank=True,null=True)
    is_active=models.BooleanField(default=True)
class Courses(models.Model):
    Course_name=models.CharField(max_length=200)
    Course_fees=models.FloatField(max_length=50)
    Course_duration=models.CharField(max_length=200)
    Course_textbox=models.TextField()
    is_active=models.BooleanField(default=True)
class Student(models.Model):
    Student_Name=models.CharField(max_length=200)
    Student_email=models.EmailField(max_length=200)
    Student_mobile_number=models.IntegerField(max_length=10)
    Student_college=models.CharField(max_length=200)
    Student_degree=models.CharField(max_length=200)
    Course_name=models.ForeignKey(Courses,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
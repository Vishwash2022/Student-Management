from django.db import models

class User(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Password=models.CharField(max_length=500,blank=True,null=True)
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.Name
class Courses(models.Model):
    Course_name=models.CharField(max_length=200)
    Course_fees=models.FloatField(max_length=50)
    Course_duration=models.CharField(max_length=200)
    Course_textbox=models.TextField()
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.Course_name
class Student(models.Model):
    Student_Name=models.CharField(max_length=200)
    Student_email=models.EmailField(max_length=200)
    Student_mobile_number=models.IntegerField(max_length=10)
    Student_college=models.CharField(max_length=200)
    Student_degree=models.CharField(max_length=200)
    Course_name=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Student_due=models.IntegerField()
    Student_paid=models.IntegerField()
    Student_total=models.IntegerField()
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.Student_name
    
class Teacher(models.Model):
    Teacher_name=models.CharField(max_length=200)
    Teacher_email=models.CharField(max_length=200)
    Teacher_mobile_number=models.IntegerField(max_length=10)
    Teacher_joining_date=models.DateField()
    Teacher_education=models.CharField(max_length=100)
    Teacher_employee_id=models.IntegerField(max_length=10)
    Teacher_work_exp=models.CharField(max_length=200)
    teacher_pack=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.Teacher_name
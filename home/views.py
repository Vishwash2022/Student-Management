from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.http import HttpResponse

def sign_in(request):
    return render(request,'index.html')
def sign_up(request):
    return render(request,'sign-up.html')
def home(request):
    return render (request,'sign-up.html')
def pg_dash(request):
    return render(request,'pg_dashboard.html')
def courses(request):
    return render(request,'courses.html')
def dash(request):
    return render(request,'dashboard.html')
def viewstudents(request):
    return render(request,'viewstudents.html')
def courses(request):
    return render(request,'courses.html')
def sign_up_data(request):
    if request.method=="POST":
        Name=request.POST['User_Name']
        Email=request.POST['User_Email']
        Password=make_password(request.POST['User_Password'])
        if User.objects.filter(Email=Email).exists():
            messages.error(request,"This Email is already exists")
            return redirect('/')
        else:
            user=User.objects.create(Name=Name,Email=Email,Password=Password) 
            user.save()
            return redirect('/''')
def sign_in_data(request):
    if request.method=="POST":
        Email=request.POST['Sign_in_Email']
        Password=request.POST['Sign_in_Password']
        if User.objects.filter(Email=Email).exists():
            obj=User.objects.get(Email=Email)
            password=obj.Password
            if check_password(Password,password):
                return redirect('/dash')
            else:
                return HttpResponse("Password incorrect")
        else:
            return HttpResponse("Email is not register")
    else:
        return HttpResponse("Something incorrect")
def add_courses(request):
    if request.method=="POST":
        Course_name=request.POST['Course']
        Course_fees=request.POST['Fees']
        Course_duration=request.POST['duration']
        Course_textbox=request.POST['Text']
        course=Courses.objects.create(Course_name=Course_name,Course_fees=Course_fees,Course_duration=Course_duration,Course_textbox=Course_textbox)
        course.save()
        messages.success(request,"Course saved succesfully")
        return render(request,'dashboard.html')
    else:
        return HttpResponse("something went wrong")
def add_student(request):
    if request.method=='POST':
        Student_Name=request.GET['Student_Name']
        Student_email=request.GET['Student_Email']
        Student_mobile_number=request.GET['Student_Mobile']
        Student_college=request.POST['Student_College']
        Student_degree=request.POST['Student_Degree']
        Course_name=request.POST['Courses']
        st=Student.objects.create(Student_Name=Student_Name,Student_email=Student_email,Student_mobile_number=Student_mobile_number,Student_college=Student_college,Student_degree=Student_degree,Course_name=Course_name)
        st.save()
        course=Courses.all()
        return render(request,'viewstudent.html',{'courses':course})
    else:
        return HttpResponse("something went wrong")
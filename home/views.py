from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        pwd=make_password(request.POST['pwd'])
        if User.objects.filter(Email=email).exists():
            messages.info(request,'Email already exists ')
            return render(request,'sign-up.html')    
        else:
            user=User.objects.create(Name=name,Email=email,Password=pwd)
            user.save()
            messages.success(request,'!!!!! Sucessfully Registered !!!!!')
            return render(request,'index.html')
    else:        
        return render(request,"sign-up.html")

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd_user=request.POST['pwd']
        if User.objects.filter(Email=email).exists():
            obj=User.objects.get(Email=email)
            pwd=obj.Password
            if check_password(pwd_user,pwd):
                return redirect('/dashboard')
            else:
                messages.error(request,' Password Incorrect')
                return render (request,'index.html')                
        else:
            messages.error(request,' email is not registered')       
            return render(request,"index.html") 
    else:       
        return render(request,"index.html")

def index(request):
    return render (request,'index.html')        

def lgout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout ')
    return render(request,'index.html') 

def course(request):
    data=Courses.objects.all()
    return render (request,'courses.html',{'data':data})
     

def addcourses(request):
    name=request.POST['name']
    fees=request.POST['fees']
    fees=int(fees)
    duration=request.POST['duration']
    textfield=request.POST['textfield']
    if Courses.objects.filter(Course_name=name).exists():
        messages.info(request,'Course already exists')
        data=Courses.objects.all()
        return render(request,'courses.html',{'data':data}) 
    else:
        Courses.objects.create(Course_name=name, Course_fees=fees,Course_textbox=textfield,Course_duration=duration)
        messages.success(request,'!!!!Successfully Added!!!!')
        data=Courses.objects.all()
        return render(request,'courses.html',{'data':data}) 

def deletecourse(request):
    cid=request.GET['cid']
    Courses.objects.get(id=cid).delete()
    data=Courses.objects.all()
    return render(request,"courses.html",{'data':data}) 

def updatecourse(request):
    c=Courses()
    c.id=request.POST['id'] 
    c.name=request.POST['name']
    fees=request.POST['fees']
    c.fees=request.POST['fees']
    c.duration=request.POST['duration']
    c.textfield=request.POST['textfield']   
    c.save()
    data=Courses.objects.all()
    return render(request,'course.html',{'data':data})

def searchcourse(request):
    name=request.POST['name']
    e=Courses.objects.get(name=name)
    return render(request,'course.html',{'data':[e]})     

def addstudent(request):
    t=Student()
    t.Student_Name=request.POST['name']
    t.Student_email=request.POST['email']
    t.Student_mobile_number=request.POST['contact']
    t.Student_college=request.POST['college']
    t.Student_degree=request.POST['degree']
    tid=request.POST['course']
    t.Student_due=request.POST['Due']
    t.Student_paid=request.POST['Paid']
    t.Student_total=request.POST['Total']
    t.Course_name=Courses.objects.get(id=tid)
    t.save()
    st=Student.objects.all()
    data=Courses.objects.all()
    return render(request,'viewstudents.html',{'st':st,'data':data})

def deletestudent(request):
    id=request.GET['id']
    Student.objects.filter(id=id).delete()
    data=Courses.objects.all()
    st=Student.objects.all()
    return render(request,'viewstudents.html',{'data':data,'st':st}) 

def updatestudent(request): 
    t=Student()
    t.id=request.POST['id']
    t.name=request.POST['name']
    t.email=request.POST['email']
    t.contact=request.POST['contact']
    t.college=request.POST['college']
    t.degree=request.POST['degree']
    tid=request.POST['course']
    t.course=Courses.objects.get(id=tid)
    t.save()
    data=Courses.objects.all()
    st=Student.objects.all()
    return render(request,'viewstudents.html',{'data':data,'st':st})

def searchstudent(request):
    find=request.POST['name']
    s=Student.objects.filter(Q(name=find) | Q(email=find) | Q(college=find)).all()
    return render(request,'viewstudents.html',{'st':s})                                   

def dashboard(request):
    data=Courses.objects.all()
    count_course= Courses.objects.all().count()
    count_student= Student.objects.all().count()
    count_teacher=Teacher.objects.all().count()
    return render (request,'dashboard.html',{'data':data,'count_course':count_course,'count_student':count_student,'count_teacher':count_teacher})

def viewstudents(request):
    data=Courses.objects.all()
    st=Student.objects.all()
    return render(request,'viewstudents.html',{'data':data,'st':st})

def Teachers(request):
    tc=Teacher.objects.all()
    return render(request, 'teacher.html',{'tc':tc})            

def addteacher(request):
        if request.method == "POST":
            name= request.POST["tname"]
            email= request.POST["temail"]
            mobile= request.POST["tmobile"]
            joining= request.POST["tjoindate"]
            education= request.POST["teducation"]
            employeeId= request.POST["tempid"]
            workExp= request.POST["tworkexpe"]
            pack=request.POST["tpack"]
            if Teacher.objects.filter(email=email).exists():
                messages.error(request, "Email id already exists")
                return redirect('teacher.html')
        
            elif Teacher.objects.filter(mobile=mobile).exists():
                messages.error(request, "Mobile Number already exists")
                return redirect('teacher.html')
            else:
                Teacher.objects.create( name=name, 
                                            email=email, 
                                            mobile=mobile,
                                            joining=joining,
                                            education=education,
                                            employeeId=employeeId,
                                            workExp=workExp,
                                            pack=pack
                                            )
                messages.success(request, "Teacher Added Successfully!!")
                tc=Teacher.objects.all()
                return render(request, 'teacher.html',{'tc':tc})
            
        else:
            tc=Teacher.objects.all()
            return render(request, 'teacher.html',{'tc':tc})

def updateteacher(request,pk):
            t=Teacher()
            t.id=pk
            t.name= request.POST["name"]
            t.email= request.POST["email"]
            t.mobile= request.POST["mobile"]
            t.joining= request.POST["joining"]
            t.education= request.POST["education"]
            t.employeeId= request.POST["employeeId"]
            t.workExp= request.POST["workExp"]
            t.pack=request.POST["pack"]
            t.save()
            tc=Teacher.objects.all()
            return render(request, 'teacher.html',{'tc':tc})
def deleteteacher(request,pk):
    id=pk
    Teacher.objects.filter(id=id).delete()
    tc=Teacher.objects.all()
    return render(request,'teacher.html',{'tc':tc})
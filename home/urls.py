from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
<<<<<<< HEAD
    path("",views.index),
    path("signin",views.signin),
    path("signup",views.signup),
    path("dashboard",views.dashboard),
    path("viewstudents",views.viewstudents),
    path("lgout",views.lgout),
    path("course",views.course),
    path("addcourses",views.addcourses),
    path('deletecourse',views.deletecourse),
    path('updatecourse',views.updatecourse),
    path('searchcourse',views.searchcourse),
    path('addstudent',views.addstudent),
    path('deletestudent',views.deletestudent),
    path('updatestudent',views.updatestudent),
    path('searchstudent',views.searchstudent),
    path('Teacher',views.Teacher),
    path('addteacher',views.addteacher,name="addTeacher")
]
=======
    path('',views.sign_in),
    path('sign_up',views.sign_up),
    path('pg_dashboard',views.pg_dash),
    path('courses',views.courses),
    path('sign_up_data',views.sign_up_data),
    path('sign_in_data',views.sign_in_data),
    path('dash',views.dash,name="dash"),
    path('viewstudents',views.viewstudents),
    path('courses',views.courses),
    path('add_courses',views.add_courses),
    path('add_student',views.add_student)
]
>>>>>>> 7e61971dc65df4e782ad5408fcb5166f7057a9a4

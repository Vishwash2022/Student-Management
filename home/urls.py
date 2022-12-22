from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index),
    
    path("signin/",views.signin,name="signin"),
    path("signup/",views.signup,name="signup"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("viewstudents/",views.viewstudents,name="viewstudent"),
    path("lgout/",views.lgout,name="lgout"),
    path("course/",views.course,name="course"),
    path("addcourses/",views.addcourses,name="addcourse"),
    path('deletecourse/',views.deletecourse,name="deletecourse"),
    path('searchcourse/',views.searchcourse,name="searchcourse"),
    path('addstudent/',views.addstudent,name="addstudent"),
    path('deletestudent/',views.deletestudent,name="deletestudent"),
    path('searchstudent/',views.searchstudent,name="searchstudent"),
    path('Teacher/',views.Teachers,name="Teacher"),
    path('addteacher/',views.addteacher,name="addTeacher"),
    path('deleteteacher/<int:pk>',views.deleteteacher,name="deleteteacher"),
    path('update/<int:pk>',views.update,name="update"),
    
    path('updatestudent/<int:pk>',views.updatestudent,name="updatestudent"),
    path('updatecourse/<int:pk>',views.updatecourse,name="updatecourse"),
    path('updatecoursedata/<int:pk>',views.updatecoursedata,name="updatecoursedata"),
    path('updateteacher/<int:pk>',views.updateteacher,name="updateteacher"),
    path('updateteacherdata/<int:pk>',views.updateteacherdata,name="updateteacherdata")
    
    
]

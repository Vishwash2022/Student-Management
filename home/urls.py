from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
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
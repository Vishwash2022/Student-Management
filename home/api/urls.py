from django.urls import path
from .api import UserModelView, UserModelView1, StudentModelView, StudentModelView1, CourseModelView, CourseModelView1, TeacherModelView, TeacherModelView1, LoginView

urlpatterns = [
    path('user/', UserModelView.as_view()),
    path('user/<int:pk>/', UserModelView1.as_view()),
    path('student/', StudentModelView.as_view()),
    path('student/<int:pk>/', StudentModelView1.as_view()),
    path('course/', CourseModelView.as_view()),
    path('course/<int:pk>/', CourseModelView1.as_view()),
    path('teacher/', TeacherModelView.as_view()),
    path('teacher/<int:pk>/', TeacherModelView1.as_view()),
    path('login/',LoginView.as_view()),
]

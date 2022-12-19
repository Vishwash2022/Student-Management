from django.urls import path
from . import views
urlpatterns = [
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

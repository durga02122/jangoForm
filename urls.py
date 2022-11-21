from django.contrib import admin
from django.urls import path,include
from .import views
from .views import about,Add_Student,Delete_Student,EditStudent


urlpatterns = [
    path('',views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('about/',about.as_view(), name='about'),
    path('add-student/',Add_Student.as_view(), name='add-student'),
    path('delete_student/', Delete_Student.as_view(), name='delete-student'),
    path('edit-student/<int:id>/', EditStudent.as_view(), name='edit-student')
]
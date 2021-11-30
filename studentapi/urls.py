from django.urls import path
from .views import CreateStudent,DeleteStudent,UpdateStudent,GetStudent,ListStudent

urlpatterns = [
    path('createapi/',CreateStudent.as_view()),
    path('deleteapi/<pk>',DeleteStudent.as_view()),
    path('updateapi/<pk>',UpdateStudent.as_view()),
    path('getstudent/',GetStudent.as_view()),
    path('liststudent/',ListStudent.as_view()),
]
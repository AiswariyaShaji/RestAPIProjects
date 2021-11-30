from django.urls import path
from .views import CreateStudent,DeleteStudent

urlpatterns = [
    path('createapi/',CreateStudent.as_view()),
    path('deleteapi/<pk>',DeleteStudent.as_view()),

]
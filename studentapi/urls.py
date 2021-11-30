from django.urls import path
from .views import CreateStudent,DeleteStudent,UpdateStudent

urlpatterns = [
    path('createapi/',CreateStudent.as_view()),
    path('deleteapi/<pk>',DeleteStudent.as_view()),
    path('updateapi/<pk>',UpdateStudent.as_view()),
]
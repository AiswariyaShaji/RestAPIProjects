from django.urls import path
from .views import CreateStudent

urlpatterns = [
    path('createapi/',CreateStudent.as_view()),
]
from django.shortcuts import render
from rest_framework import generics 
from .serializers import StudentSerializer
from .models import Student
# Create your views here.

class CreateStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DeleteStudent(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


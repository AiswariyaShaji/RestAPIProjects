from django.shortcuts import render
from rest_framework import generics 
from .serializers import StudentSerializer,ListStudentSerializer
from .models import Student
# Create your views here.

class CreateStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DeleteStudent(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudent(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class GetStudent(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ListStudent(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = ListStudentSerializer
from rest_framework import serializers
from .models import Student,Subject

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ListStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name',)
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
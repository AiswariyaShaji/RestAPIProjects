from django.db import models

# Create your models here.
class Student(models.Model):
    regno = models.IntegerField()
    name = models.CharField(max_length=50)
    standard = models.SmallIntegerField()
    marks = models.IntegerField()
    def __str__(self):
        return str(self.regno) + ' : '+ " " + self.name

class Subject(models.Model):
    regnum = models.ForeignKey(Student,on_delete = models.CASCADE)
    maths = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()
    socialscience = models.IntegerField()
    def __str__(self):
        return str(self.regnum)


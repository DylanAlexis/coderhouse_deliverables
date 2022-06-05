from django.db import models
import uuid

class Course(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4(), primary_key=True)
    c_title = models.CharField(max_length=50)
    c_lenght = models.IntegerField()

class Professor(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4(), primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default='')
    email = models.EmailField()
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

class Alumn(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4(), primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default='')
    email = models.EmailField()
    professor = models.ForeignKey(Professor, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

from django.db import models
import uuid

class Course(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4(), primary_key=True)
    c_title = models.CharField(max_length=50)
    c_lenght = models.IntegerField()

    def __str__(self) -> str:
        return self.c_title+" | "+str(self.c_lenght)+" semanas"

class Professor(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4(), primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default='')
    email = models.EmailField()
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name+" "+self.last_name+" | "+self.course.c_title

class Alumn(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4(), primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default='')
    email = models.EmailField()
    professor = models.ForeignKey(Professor, default='900af8b5-8381-4dcb-a264-538d80836ddc', null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, default='ac798626-727a-453d-b626-167f54f5912b', null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name+" "+self.last_name+" | "+self.course.c_title

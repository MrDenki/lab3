from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Учитель'),
        ('head_teacher', 'Завуч'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='teacher')
    room_number = models.CharField(max_length=10, null=True, blank=True)


class Class(models.Model):
    name = models.CharField(max_length=10)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='classes')

    def __str__(self):
        return f'{self.name}'


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Lesson(models.Model):
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lessons')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()
    lesson_number = models.IntegerField()


class Student(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    quarter = models.IntegerField()

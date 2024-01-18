from django.contrib import admin
from .models import User, Class, Subject, Lesson, Student, Grade


# Регистрируем модель User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'role', 'room_number')


# Регистрируем модель Class
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')


# Регистрируем модель Subject
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Регистрируем модель Lesson
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('school_class', 'subject', 'teacher', 'day_of_week', 'lesson_number')


# Регистрируем модель Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'school_class')


# Регистрируем модель Grade
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'quarter')

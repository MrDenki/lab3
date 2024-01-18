from rest_framework import viewsets
from .models import Class, Subject, Lesson, Student, Grade, User
from .serializers import ClassSerializer, SubjectSerializer, LessonSerializer, StudentSerializer, GradeSerializer, \
    UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "classes/<int:pk>/": "http://127.0.0.1:8000/api/classes/",

            "subjects/<int:pk>/": "http://127.0.0.1:8000/api/subjects/",

            "lessons/<int:pk>/": "http://127.0.0.1:8000/api/lessons/",

            "students/<int:pk>/": "http://127.0.0.1:8000/api/students/",

            "grades/<int:pk>/": "http://127.0.0.1:8000/api/grades/",

            "auth/users/": "http://localhost:8000/api/auth/users/",
            "auth/users{id}/": "http://localhost:8000/api/auth/users/{id}/",

            "auth/token/login/<token>": "http://localhost:8000/api/auth/token/login/",
            "auth/token/logout/": "http://localhost:8000/api/auth/token/logout/",
            "auth/token/refresh/": "http://localhost:8000/api/auth/token/refresh/",

            "auth/password/reset/": "http://localhost:8000/api/auth/password/reset/",
            "auth/password/reset/confirm/": "http://localhost:8000/api/auth/password/reset/confirm/",

        })


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = ['IsAu']


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

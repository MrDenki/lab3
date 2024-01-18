from django.urls import path, include
from .views import ClassViewSet, SubjectViewSet, LessonViewSet, StudentViewSet, GradeViewSet, APIRootView

urlpatterns = [
    path('all/', APIRootView.as_view(), name='api-root'),

    path('classes/', ClassViewSet.as_view({'get': 'list', 'post': 'create'}), name='class-list'),
    path('classes/<int:pk>/', ClassViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='class-detail'),

    path('subjects/', SubjectViewSet.as_view({'get': 'list', 'post': 'create'}), name='subject-list'),
    path('subjects/<int:pk>/', SubjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='subject-detail'),

    path('lessons/', LessonViewSet.as_view({'get': 'list', 'post': 'create'}), name='lesson-list'),
    path('lessons/<int:pk>/', LessonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='lesson-detail'),

    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='student-detail'),

    path('grades/', GradeViewSet.as_view({'get': 'list', 'post': 'create'}), name='grade-list'),
    path('grades/<int:pk>/', GradeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='grade-detail'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

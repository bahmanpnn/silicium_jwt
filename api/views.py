from rest_framework import viewsets,permissions
from .models import Course
from .serializers import CourseSerializer,UserSerializer
from django.contrib.auth.models import User

class CourseView(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(permissions.IsAdminUser,)

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import CustomUser as User
from .serializers import UserSerializer
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
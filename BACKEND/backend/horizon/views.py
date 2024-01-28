from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializer import UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

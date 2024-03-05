from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from instagram.models import User
from serializer import UserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginAPIView(APIView):
    ...

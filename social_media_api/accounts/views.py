from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        # registration logic
        return Response({"detail": "registered"}, status=status.HTTP_201_CREATED)

class LoginView():
    pass

class ProfileView():
    pass


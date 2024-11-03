# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt
# from .serializers import CustomUser, CustomUserDetailsSerializer
# @csrf_exempt
# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         email = request.data.get['email']
#         password = request.data.get['password']
#         if email == "takatokomada@gmail.com" and password == "20050605":
#             return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#         return Response({"message": "Login Error"}, status=status.HTTP_401_UNAUTHORIZED)
# views.py
# from django.contrib.auth.models import User
from .models import CustomUser, Account
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

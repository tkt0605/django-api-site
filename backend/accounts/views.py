from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get['email']
        password = request.data.get['password']
        if email == "takatokomada@gmail.com" and password == "20050605":
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"message": "Login Error"}, status=status.HTTP_401_UNAUTHORIZED)
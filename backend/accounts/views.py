from django.shortcuts import render
from .serializers import CustomUserDetailsSerializer
from accounts.models import CustomUser, Account
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserDetailsSerializer(request.user)

        return Response(serializer.data)
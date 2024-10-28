from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# @api_view(['GET'])
class HelloWorld(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'message': "Hello! authenticated user!"})
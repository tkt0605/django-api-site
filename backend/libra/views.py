import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
def google_books_search(query):
    api_key = "AIzaSyAXe-5178p1Hyl9iG1uHhEPfSMVz7b2jB4"
    if not query:
        return JsonResponse({"Error": "This isn't query"}, status=400)
    urls = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}"
    resopnse = requests.get(urls)
    if resopnse.status_code == 200:
        return JsonResponse(resopnse.json(), safe=False)
    else:
        return JsonResponse({'Error': "Failed to fetch data from Google Books API."}, status=500)
class BookViewSet(viewsets.ModelViewSet):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer 
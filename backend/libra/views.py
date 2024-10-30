import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import uuid
from django.db.models import Q
import environ
env = environ.Env()
api_key=env('API_KEY')
@api_view(['POST'])
@csrf_exempt
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return  Response(serializer.errors, status=400)
def google_books_search(request):
    query = request.GET.get('q')
    if not query:
        return JsonResponse({"Error": "This isn't query"}, status=400)
    urls = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}"
    resopnse = requests.get(urls)
    if resopnse.status_code == 200:
        return JsonResponse(resopnse.json(), safe=False)

    response_data = resopnse.json().get('items', [])
    existing_isbn13 = set(Book.objects.values_list('isbn_13', flat=False))
    existing_isbn10 = set(Book.objects.values_list('isbn_10', flat=False))
    new_books = [
        book for book in response_data
        if 'isbn_13' in get_isbn(book) and get_isbn(book)['isbn_13'] not in existing_isbn13 or existing_isbn10 
    ]
    return Response(new_books, status=False)
    
class BookViewSet(viewsets.ModelViewSet):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer 
def get_isbn(book):
    identifiers = book.get('volumeInfo', {}).get('industryIdentifiers', [])
    isbn_data = {identifier['type']: identifier['identifier'] for identifier in identifiers}
    return isbn_data
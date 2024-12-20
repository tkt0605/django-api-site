import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework import viewsets, generics
from .models import Book, Order
from accounts.models import CustomUser, Account
from .serializers import BookSerializer, OrderSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import uuid
from django.db.models import Q
from django.core.files.base import ContentFile
import environ
env = environ.Env()
api_key=env('API_KEY')
@api_view(['POST'])
# @csrf_exempt
def add_book(request):
    image = request.GET.get('image')
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
        book_instance = serializer.save(commit=False)
        if image:
            image_response = requests.get(image)
            if image_response.status_code == 200:
                image_content = ContentFile(image_response.content)
                book_instance.image.save(f"{book_instance.title}.jpg", image_content, save=True)
        book_instance.save()
        return  Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
@api_view(['GET'])
def check_book(request, isbn):
    # 指定されたISBNでデータベースを検索
    is_add = Book.objects.filter(isbn_13=isbn).exists() or Book.objects.filter(isbn_10=isbn).exists()
    return Response({'is_added': is_add})
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
    # existing_isbn10 = set(Book.objects.values_list('isbn_10', flat=False))
    new_books = [
        book for book in response_data
        if 'isbn_13' in get_isbn(book) and get_isbn(book)['isbn_13'] not in existing_isbn13 
    ]
    return Response(new_books, status=False)
    
class BookViewSet(viewsets.ModelViewSet):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer 
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
def get_isbn(book):
    identifiers = book.get('book.volumeInfo', {}).get('industryIdentifiers', [])
    isbn_data = {identifier['type']: identifier['identifier'] for identifier in identifiers}
    return isbn_data
class BooksListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BooksDeatilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
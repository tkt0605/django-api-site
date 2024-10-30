from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from .views import google_books_search
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('book', views.BookViewSet)
urlpatterns = [
      path('search/', views.google_books_search, name='google_books_search'),
      path('books/', views.add_book, name='add_book'),
      path('', include(router.urls))
]
if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
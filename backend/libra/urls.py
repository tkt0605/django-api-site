from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from .views import google_books_search
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('book', views.BookViewSet)
router.register('order', views.OrderViewSet)
router.register("users", views.CustomUserViewSet)
router.register('account', views.AccountViewSet)
urlpatterns = [
      path('search/', views.google_books_search, name='google_books_search'),
      path('add/book/', views.add_book, name='add-book'),
      path('books/', views.BooksListView.as_view(), name='booklist'),
      path('books/<uuid:pk>', views.BooksDeatilView.as_view(), name='bookdetails'),
      path("orders/", views.OrderListView.as_view(), name="orderlist"),
      path('orders/<uuid:pk>', views.OrderDetailView.as_view(), name='orderdetail'),
      path('', include(router.urls))
]
if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
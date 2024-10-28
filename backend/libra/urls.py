from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HelloWorld
urlpatterns = [
       path('hello/',HelloWorld.as_view(), name='helloworld'),
]
if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HelloWorld
urlpatterns = [
       path('api/home',HelloWorld.as_view(), name='helloworld'),
]

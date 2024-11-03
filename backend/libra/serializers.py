from rest_framework import serializers  
from .models import Book, Order
from accounts.models import Account, CustomUser

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class AccountSerializr(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
class CustomUserSerializr(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
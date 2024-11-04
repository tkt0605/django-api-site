from .models import CustomUser, Account
from rest_framework import serializers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # passwordをwrite_onlyに設定

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'is_staff', 'is_active', 'is_superuser')  # 必須フィールドを指定

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])  # パスワードを暗号化して保存
        user.save()
        return user
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
    def create(self, validated_data):
        user = Account(
            email=validated_data['email'],
            name=validated_data['name'],
            icon = validated_data['icon'],
            explain = validated_data['explain']
        )
        user.save()
        return user
# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     email = serializers.EmailField(required=True)

#     def validate(self, attrs):
#         # email と password を取得
#         email = attrs.get('email')
#         password = attrs.get('password')

#         # ユーザー認証
#         user = authenticate(request=self.context.get('request'), username=email, password=password)
#         if not user:
#             raise serializers.ValidationError("Invalid credentials")

#         # TokenObtainPairSerializerのvalidateメソッドを呼び出す
#         attrs['username'] = user.username
#         return super().validate(attrs)
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        # email と password を取得
        email = attrs.get('email')
        password = attrs.get('password')

        # デバッグメッセージ
        print("Received email:", email)
        print("Received password:", password)

        # ユーザー認証
        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if not user:
            print("Authentication failed: Invalid credentials")
            raise serializers.ValidationError("Invalid credentials")
        
        print("Authentication successful for user:", user)
        
        # TokenObtainPairSerializerのvalidateメソッドを呼び出す
        attrs['username'] = user.username
        return super().validate(attrs)
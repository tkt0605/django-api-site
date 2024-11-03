# from accounts.models import CustomUser, Account
# from rest_framework import serializers

# class CustomUserDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser  # シリアライズ対象のモデル
#         fields = "__all__"  
# class AccountSerializr(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = "__all__"
# serializers.py
from .models import CustomUser, Account
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

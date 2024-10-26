from accounts.models import CustomUser, Account
from rest_framework import serializers

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # シリアライズ対象のモデル
        fields = ('id', 'email', 'username')  
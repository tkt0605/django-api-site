from .models import CustomUser, Account
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # passwordをwrite_onlyに設定

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')  # 必須フィールドを指定

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])  # パスワードを暗号化して保存
        user.save()
        return user
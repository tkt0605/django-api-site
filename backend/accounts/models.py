from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group, PermissionsMixin
from django.utils import timezone
from django.conf import settings
from rest_framework.authtoken.models import Token
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("Emailアドレスが必要です。")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractUser, PermissionsMixin):
    email = models.CharField(max_length=319, unique=True)
    username = models.CharField(max_length=75, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    join_date=models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()

    groups = models.ManyToManyField(Group, related_name="custom_user_group", blank=True, help_text="このユーザーが所属するグループ。ユーザーは、各グループに付与されたすべての権限を取得します", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True, help_text="このユーザーに対する特定の権限", related_query_name="user")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    def __str__(self):
        return self.email
    @property 
    def profile(self):
        return Account.objects.get_or_create(user=self)[0]
    @property
    def token(self):
        return Token.objects.get_or_create(user=self)[0]
class Account(models.Model):
    email = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='Emailアドレス', blank=True, null=True)
    name = models.CharField(max_length=75, verbose_name='ユーザー名', blank=True, null=True)
    icon = models.ImageField(upload_to='icon/', verbose_name='アイコン',  default='icon/kkrn_icon_user_1.png')
    explain = models.TextField(max_length=200, verbose_name='紹介文', blank=True, null=True, default="今は公開プロフィールはありません。\nご自身についての情報を追加しましょう。")
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Account'
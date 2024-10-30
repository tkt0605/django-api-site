from django.db import models
import uuid
from django.utils import timezone
    # id INT AUTO_INCREMENT PRIMARY KEY,
    # title VARCHAR(50) NOT NULL,
    # author VARCHAR(50),  -- 'auther' を 'author' に修正
    # isbn VARCHAR(13) UNIQUE NOT NULL,
    # description TEXT,
    # stock INT DEFAULT 0,
    # price DECIMAL(10, 2) NOT NULL,
    # created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name='タイトル')
    publisher = models.CharField(max_length=255, verbose_name="出版社")  
    publish_date = models.DateField()
    author = models.CharField(max_length=100, verbose_name='作者')
    stock = models.IntegerField(verbose_name="在庫数")
    price = models.IntegerField(verbose_name='価格')
    isbn_10 = models.CharField(max_length=10, blank=True, null=True)  # ISBN_10
    isbn_13 = models.CharField(max_length=13, blank=True, null=True)  # ISBN_13
    language = models.CharField(max_length=10, default='ja')  # 言語
    crated_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    
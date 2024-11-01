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
    image = models.ImageField(upload_to='image/', verbose_name="表紙", null=True,blank=True)
    publisher = models.CharField(max_length=255, verbose_name="出版社")  
    publish_date = models.DateField()
    author = models.CharField(max_length=100, verbose_name='作者')
    stock = models.IntegerField(verbose_name="在庫数",blank=True, null=True)
    price = models.IntegerField(verbose_name='価格',blank=True, null=True)
    isbn_10 = models.CharField(max_length=10, blank=True, null=True)  # ISBN_10
    isbn_13 = models.CharField(max_length=13, blank=True, null=True)  # ISBN_13
    language = models.CharField(max_length=10, default='ja')  # 言語
    crated_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[('pending', '注文待ち'), ('shipped', '配送済み'), ('delivered', '配達完了')])
    def __str__(self):
        return self.book
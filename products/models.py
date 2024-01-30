from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid5,
        editable=False
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.SmallIntegerField()
    cover = models.ImageField(upload_to='covers/', blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.category}"
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    
    
class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.review
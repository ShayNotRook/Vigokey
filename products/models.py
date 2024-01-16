from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.SmallIntegerField()
    
    def __str__(self):
        return f"{self.title} - {self.category}"
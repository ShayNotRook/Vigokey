from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

def user_image_path(instance, filename):
    return f'user_{instance.id}/{filename}'

class CustomUser(AbstractUser):
    name = models.CharField(("Name of user"), blank=True, null=True, max_length=255)
    is_verified = models.BooleanField(default=False)
    
    # def get_absolute_url(self):
    #     return reverse('accounts:detail', kwargs={'username': self.username})
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(upload_to=user_image_path, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    newsletter_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name_plural = 'User Profile'
    
    
class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.user.name} - {self.balance}"
    
    
CustomUser.wallet = property(lambda u: Wallet.objects.get_or_create(user=u)[0])
    
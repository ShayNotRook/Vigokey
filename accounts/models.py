from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

def user_image_path(instance, filename):
    return f'user_{instance.id}/{filename}'

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to=user_image_path, null=True, blank=True)
    
    
class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.user.name} - {self.balance}"
    
    
CustomUser.wallet = property(lambda u: Wallet.objects.get_or_create(user=u)[0])
    
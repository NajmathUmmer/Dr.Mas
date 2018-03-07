from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser

# Create your models here.
class allusers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='mas/static/images/', blank=True, default='')
    age = models.IntegerField()
    sex= models.CharField(max_length=10)
    def __str__(self):
				 return str(self.user)
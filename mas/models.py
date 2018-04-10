from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser


# Create your models here.
class Allusers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='mas/static/images/', blank=True, default='mas/static/images/download.jpg', null=True)
    age = models.IntegerField()
    sex= models.CharField(max_length=10)
    def __str__(self):
				 return str(self.user)


class Disease(models.Model):
	did=models.IntegerField()
	diagnose=models.CharField(max_length=50)
	description = models.URLField(max_length=128,default='')
	def __str__(self):
				 return str(self.diagnose)

class Symptom(models.Model):
	syd=models.IntegerField()
	symptoms=models.CharField(max_length=50)
	sex=models.CharField(max_length=10,default='')

	def __str__(self):
				 return str(self.symptoms)
	
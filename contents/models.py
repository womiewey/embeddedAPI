from django.db import models
# from misc import get_upload_path
# Create your models here.

class userAdmin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__ (self):
        return self.username,password

class userProfile(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    patient = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    face = models.ImageField(upload_to='pic_folder/faces/', default= 'pic_folder/None/no-img.jpg')
    eye = models.ImageField(upload_to='pic_folder/eyes/', default='pic_folder/None/no-eyemg.jpg')

    def __str__ (self):        
        return self.lastname,firstname



    
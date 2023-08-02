from django.db import models

# Create your models here.
class Appinfo(models.Model):
    name = models.CharField(max_length=50)
    carousel1 = models.ImageField(upload_to= 'carousel')
    carousel2 = models.ImageField(upload_to= 'carousel')
    carousel3 = models.ImageField(upload_to= 'carousel')
    carousel4 = models.ImageField(upload_to= 'carousel', null=True)
    carousel5 = models.ImageField(upload_to= 'carousel', null=True)
    logo = models.ImageField(upload_to='logo')  
    copyright = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='nominees', null=True)
    details = models.CharField(max_length=50, null=True)  
    
      
      
    def __str__(self):
          return self.title

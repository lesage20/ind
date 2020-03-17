from django.db import models

# Create your models here.
class Detail(models.Model):
    
    nom = models.CharField(max_length=70)
    contenu = models.TextField()
    message = models.TextField()
    image = models.ImageField(upload_to="images/detail")
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(True)
    
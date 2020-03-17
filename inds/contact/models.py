from django.db import models

# Create your models here.

class Contact(models.Model):
    
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    icone = models.ImageField(upload_to="images/Contact")
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    satus = models.BooleanField(True)
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        
    def __str__(self):
        return self.nom

class Newsletter(models.Model):
    
    email = models.EmailField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    satus = models.BooleanField(True)
    
    class Meta:
        verbose_name = "News letter"
        verbose_name_plural = "News Letters"
    
    def __str__(self):
        return self.email
    
        
from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100, blank=True)
    thumbnail= models.ImageField(upload_to='thumbnail')
    link = models.URLField(max_length=200)
    pdf = models.FileField(upload_to='PDFs')
    author =models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    

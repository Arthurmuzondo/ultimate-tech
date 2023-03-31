from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_images')
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
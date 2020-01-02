from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.TextField(max_length=900)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=200)
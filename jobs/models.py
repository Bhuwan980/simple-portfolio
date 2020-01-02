from django.db import models

class Jobs(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.TextField(max_length=200)

	
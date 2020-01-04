from django.db import models

class Jobs(models.Model):
	title = models.CharField(max_length=200, default='')
	image = models.ImageField(upload_to='images/')
	summary = models.TextField(max_length=500)


	def __str__(self):
		return self.title

	
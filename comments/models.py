from django.db import models

# Create your models here.

class Comment(models.Model):
	username = models.CharField(max_length=20)
	context = models.TextField()
	create_time = models.DateTimeField(auto_now_add=True)




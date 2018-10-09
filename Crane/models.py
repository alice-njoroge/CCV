from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
	username = models.CharField(max_length=20)
	message = models.TextField()
	email = models.EmailField()


# Create your models here.

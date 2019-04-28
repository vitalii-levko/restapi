from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	body = models.TextField()

	class Meta:
		ordering = ('created',)


class User(AbstractUser):
	username = models.CharField(max_length=100, unique=True)
	email = models.EmailField('email address', unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	def __str__(self):
		return "{}".format(self.email)

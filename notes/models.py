from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	"""
	Connects user table to notes table
	CASCADE means that if a user is deleted, all their notes will be deleted as well
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
	
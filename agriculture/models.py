from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Complain(models.Model):
	name = models.CharField(max_length=50)
	phone_no = models.IntegerField()
	complain = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('agriculture')


class Agriculture(models.Model):
	scheme_name= models.CharField(max_length=100)
	scheme_name_hindi = models.CharField(max_length=100,default='')
	scheme_discription = models.TextField()
	scheme_discription_hindi = models.TextField(default='')
	scheme_image = models.ImageField(default='default.jpg')

	def __str__(self):
		return self.scheme_name


class Training(models.Model):
	video_title = models.CharField(max_length=100)
	video_title_hindi = models.CharField(max_length=100,default='')
	url = models.CharField(max_length=500)

	def __str__(self):
		return self.video_title


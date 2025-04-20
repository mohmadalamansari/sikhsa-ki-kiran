from django.db import models

class Subject(models.Model):
	subject_name = models.CharField(max_length=50)
	subject_name_hindi = models.CharField(max_length=50,default='')
	subject_image = models.ImageField(default= 'default.jpg')

	def __str__(self):
		return self.subject_name

class Topic(models.Model):
	topic_name = models.CharField(max_length=50)
	topic_name_hindi = models.CharField(max_length=50,default='')
	topic_image = models.ImageField(default='default.jpg')
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

	def __str__(self):
		return self.topic_name


class Video(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
	url =  models.CharField(max_length=500)
	video_title = models.CharField(max_length=100, default ='')
	video_title_hindi = models.CharField(max_length=100, default ='')

	def __str__(self):
		return self.video_title
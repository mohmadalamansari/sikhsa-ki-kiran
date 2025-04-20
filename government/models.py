from django.db import models

class GovernmentSchemes(models.Model):
	scheme_name = models.CharField(max_length=100)
	scheme_name_hindi = models.CharField(max_length=100,default='')
	scheme_image = models.ImageField()
	scheme_url = models.CharField(max_length=500,default ='')

	def __str__(self):
		return self.scheme_name
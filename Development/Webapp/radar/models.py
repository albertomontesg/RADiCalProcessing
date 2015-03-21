from django.db import models

# Create your models here.

class Speed(models.Model):
	date_time = models.DateTimeField('data_time', auto_now_add = True)
	speed = models.DecimalField('speed',max_digits=5, decimal_places = 2)

	def __str__(self):
		return 'Speed: ' + str(self.speed) + ' km/h\tDate Time: ' + str(self.date_time)
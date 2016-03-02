from django.db import models

# Create your models here.

class Restaurant(models.Model):
	restaurant_name = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date created')
	def __str__(self):
		return self.restaurant_name

class Menu(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	menu_name = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.menu_name
	

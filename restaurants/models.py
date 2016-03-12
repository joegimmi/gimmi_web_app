from django.db import models

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length=50)
	creation_date = models.DateTimeField('date created')
	description = models.CharField(max_length = 200)
	website = models.CharField(max_length = 100)
	phone = models.CharField(max_length=40)
	address=models.CharField(max_length=100)
	picture = models.ImageField(upload_to='images/') #add null=true if allow empty (and blank will need to be added to)
	email = models.EmailField()
	#open_time=models.TimeField() I need to add open and closing time for every day of the week. Thought of method but testing this first 
	#close_time=models.TimeField()
	
	def __str__(self):
		return self.restaurant_name

class Menu(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)


	def __str__(self):
		return self.menu_name
	
class Item(models.Model):
	menu=models.ForeignKey(Menu, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	picture = models.ImageField(upload_to='images/', null=True, blank=True)
	price = models.DecimalField(max_digits=7,decimal_places=2)


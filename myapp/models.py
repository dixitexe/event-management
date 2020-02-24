from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	mobile=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	cpassword=models.CharField(max_length=200)
	status=models.CharField(max_length=200,default="inactive")

	def __str__(self):
		return self.fname+" "+self.lname

class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	mobile=models.CharField(max_length=200)
	remarks=models.TextField()

	def __str__(self):
		return self.name

class Event(models.Model):
	EVENT_CHOICES = [
    ('Sports', 'Sports'),
    ('Concerts', 'Concerts'),
    ('Political', 'Political')
	]
	event_category = models.CharField(choices=EVENT_CHOICES,max_length=100)
	event_name=models.CharField(max_length=200)
	event_desc=models.TextField()
	event_price=models.CharField(max_length=200)
	event_image=models.ImageField(upload_to='images/',blank=True,null=True)

	def __str__(self):
		return self.event_name

class Book_Event(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	event=models.ForeignKey(Event,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
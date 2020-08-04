from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 
from django.db.models.signals import post_save

# Create your models here.

class Customer(models.Model):
	user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic=models.ImageField(null=True,blank=True,default="pic.png")
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	note=models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name




class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
    
	def __str__(self):
		return str(self.product.name)

# class Profile(models.Model):
# 	user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
# 	first_name=models.CharField(max_length=100, null=True, blank=True)
# 	last_name=models.CharField(max_length=100, null=True, blank=True)
# 	phone=models.CharField(max_length=100,null=True,blank=True)

# 	def __str__(self):
# 		return str(self.first_name)
	
# def create_profile(sender,instance,created,**kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)
# 		print("Profile created")

# post_save.connect(create_profile,sender=User)

# def update_profile(sender,instance,created,**kwargs):
# 	if created==False:
# 		instance.profile.save()
# 		print("Profile updated")
# post_save.connect(update_profile,sender=User)



	
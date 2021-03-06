from freelancesolution.enums import ProductType
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Product(models.Model):
	name = models.CharField(max_length = 200)
	description = models.TextField()
	price = models.IntegerField(default = 0)
	product_type = models.CharField(max_length=15, choices=[(tag.name, tag.value) for tag in ProductType], null = True, blank = True)
	img = models.ImageField(upload_to = 'products')
	high_res = models.ImageField(upload_to = 'products', null = True, blank = True)

	def __str__(self):
		return self.name

# The 'connection' between Users and Products, to achieve a Many To Many relation
class UserProduct(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)

	def __str__(self):
		return f'{self.user.username}: {self.product.name}'


class ProductReview(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	review = models.TextField()
	date_created = models.DateTimeField(default = timezone.now)
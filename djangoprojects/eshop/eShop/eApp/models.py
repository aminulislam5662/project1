from datetime import datetime
from operator import mod
import os

from turtle import ondrag, up
from django.db import models
from django.utils.timezone import datetime


from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


def filepath(request,filename):
  timenow = datetime.now()
  filename = "%s%s" % (timenow,filename)
  return os.path.join('static/productimage/',filename)


class ProductImages(models.Model):
    file = models.FileField(upload_to=filepath)

class products(models.Model):
    product_id= models.TextField(max_length=255)
    title = models.TextField(max_length=255)
    oldprice = models.TextField(max_length=255)
    newprice = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    specification = models.TextField(max_length=255)
    reviews = models.TextField(max_length=255)
    comments = models.TextField(max_length=255)
    image = models.FileField(upload_to=filepath)
    productImages= models.OneToOneField(ProductImages,on_delete=models.CASCADE)


#######################################################################

class Interests(models.Model):
  title = models.CharField(max_length=200)

  def __str__(self):
      return self.title

class City(models.Model):
  title= models.CharField(max_length=200)

  def __str__(self):
      return self.title

class Mobile(models.Model):
  mobile= models.CharField(max_length=20)

  def __str__(self):
      return self.mobile


class Person(models.Model):
  name= models.CharField(max_length=200)
  mobile= models.OneToOneField(Mobile,on_delete=models.CASCADE)
  interests= models.ManyToManyField(Interests)

  def __str__(self):
      return self.name


class PersonAddress(models.Model):
  person= models.OneToOneField(Person, on_delete=models.CASCADE)
  city= models.ForeignKey(City,on_delete=models.CASCADE)
  street_address= models.CharField(max_length=200)

  def __str__(self):
      return self.person.name + "(" + self.street_address + ")"





class Post(models.Model):
    # user = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)
  
def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "static/productimage/%s-%s" % (slug, filename)  


class Images(models.Model):
    post = models.ForeignKey(Post, default=None,on_delete=models.CASCADE)
    image = models.FileField(upload_to=get_image_filename,
                              verbose_name='Image')







# class Post(models.Model):
#     title = models.CharField(max_length=250)
#     description = models.TextField()
#     image = models.FileField(blank=True)
 
#     def __str__(self):
#         return self.title
 
# class PostImage(models.Model):
#     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
#     images = models.FileField(upload_to = 'static/images/')
 
#     def __str__(self):
#         return self.post.title
# # # Create your models here.


# class bags(models.Model):
# 	brand = models.CharField(max_length=50)
# 	capacity=models.CharField(max_length=10)

# 	def __str__(self):
# 		return "%s" % (self.brand)

# class buyers(models.Model):
# 	name = models.CharField(max_length=70)
# 	age = models.IntegerField()
# 	bags_purchased = models.ManyToManyField(bags)		

# 	def __str__(self):
# 		return "%s" % (self.name)



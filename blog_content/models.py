from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=255)
	overview = models.TextField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now_add=True)
	categories = models.ManyToManyField(Category, related_name='posts')
	tags = models.ManyToManyField(Tag, related_name='posts')

	def __str__(self):
		return self.title



class Comment(models.Model):
	author = models.CharField(max_length=255)
	body = models.TextField()
	created_on = models.DateTimeField
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return self.author


class Author(models.Model):
	avatar = models.ImageField(upload_to="avatar/")
	name = models.CharField(max_length=100)
	overview = models.TextField()

	def __str__(self):
		return self.name

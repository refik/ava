from django.db import models
import datetime

class Vote(models.Model):
	date = models.DateTimeField('dateV')
	choice = models.CharField(max_length=10)
	info = models.CharField(max_length=400)
	def __unicode__(self):
		return self.choice

class Comment(models.Model):
	vote = models.ForeignKey(Vote)
	choice=models.CharField(max_length=10)
	name = models.CharField(max_length=10)
	text = models.CharField(max_length=500)
	like = models.IntegerField()
	date = models.DateTimeField('dateC')
	email= models.EmailField()
	def __unicode__(self):
		return self.text

class Count(models.Model):
	apple = models.IntegerField()
	adobe = models.IntegerField()

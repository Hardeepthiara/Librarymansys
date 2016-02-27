from __future__ import unicode_literals

from django.db import models

# Create your models here.
class sep(models.Model):
	name=models.CharField(max_length=10)
	bio=models.CharField(max_length=50)
	des=models.TextField(max_length=100)
	twitter=models.CharField(max_length=50,blank=True)
	facebook=models.CharField(max_length=50,blank=True)

	def __str__(self):
		return self.name

class mno(models.Model):
	name=models.CharField(max_length=10)
	bio=models.CharField(max_length=50)
	def __str__(self):
		return self.name
	

class track(models.Model):
	name=models.CharField(max_length=10)
	abstract=models.TextField(max_length=100)
	Sep=models.ForeignKey(sep)
	Mno=models.ForeignKey(mno)
	def __str__(self):
		return self.name
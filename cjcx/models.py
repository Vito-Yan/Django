# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    Sno=models.CharField(max_length=9,primary_key=True)
    Sname=models.CharField(max_length=20,unique=True)
    Sdept=models.CharField(max_length=20)
    Spwd=models.CharField(max_length=20)

class Course(models.Model):
#	Cno=models.CharField(max_length=2,primary_key=True)
	Cname=models.CharField(max_length=30,unique=True,primary_key=True)
	Credit=models.DecimalField(max_digits=2, decimal_places=1)

class SC(models.Model):
	Sno=models.CharField(max_length=9)
#	Cno=models.CharField(max_length=2)
	Cname=models.CharField(max_length=30)
	Grade=models.IntegerField()
	class Meta:
		unique_together = (("Sno", "Cname"),)

	def __unicode__(self):
		return self.Sno

	def __unicode__(self):
		return self.Cname

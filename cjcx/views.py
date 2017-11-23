# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
	return render(request, 'jwcjcx.html')

def search_action(request):
	Sno = request.POST['Sno']
	Spwd = request.POST['Spwd']
#这里放爬虫和数据入库的代码。。。。。
	student = models.Student.objects.get(Sno=Sno)
	pwd = student.Spwd
	if Spwd==pwd:
		sc = models.SC.objects.filter(Sno=Sno)
#		course = models.Course.objects.filter(Cname=sc.Cname)
		return render(request,'jwcjcx.html',{'student':student, 'sc':sc})


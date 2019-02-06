# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Contact

# Create your views here.

#displays stuff on browser

def index(request):
	return render(request, 'mysite/index.html')

def portfolio(request):
	return render(request, 'mysite/portfolio.html')

def blog(request):
	return render(request, 'mysite/blog.html')

def contact(request):
	if request.method == 'POST':
		nameR = request.POST.get('name')
		lastNameR = request.POST.get('lastName')
		emailR = request.POST.get('email')
		subjectR = request.POST.get('subject')
		messageR = request.POST.get('message')

		newContact = Contact(name=nameR, lastName=lastNameR, email=emailR, subject=subjectR, message=messageR)
		newContact.save()

		return render(request, 'mysite/contact.html')
	else:
		return render(request, 'mysite/contact.html')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import ContactForm
from django.shortcuts import render_to_response

# Create your views here.

def current_date_time(request):
	now = datetime.datetime.now()
	html = "<html> <body> It is now %s. </body></html>"% now
	return HttpResponse(html)


def hours_after(request, offset):
	offset = int(offset)
	now = datetime.datetime.now()
	dt = now + datetime.timedelta(hours=offset)
	html = "<html> <body> It is now %s. %s after %s</body></html>"% (now,offset,dt)
	print("I am here")
	return HttpResponse(html)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			topic = form.cleaned_data['topic']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			print("topic %s message %s sender %s"%(topic,message,sender))

	else:
		form = ContactForm()
	return render(request,'contacts.html', {'form': form})
from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponse
import re
import feedparser

# Create your views here.

def feed(request):
	return render(request, 'rss_feed/home.html')

def search(request):
    if 'q' in request.GET:
    	try:
    		d = feedparser.parse(request.GET['q'])
    		s = d['feed']['title'] + '\n' +  d['feed']['description'] + '\n'
    		for post in d.entries:
        		s = s + '\n' + post.title + '\n'
        		sm = post.summary
        		sm = re.sub('<.*?>','',sm)
        		s = s + '\n' + sm + '\n'
    		for post in d.entries:
    			s = s + post.link
    		models.link(url = request.GET['q']).save()
    		return HttpResponse(s)
    	except KeyError:
    		return HttpResponse("You submitted an invalid rss feed")
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)
    

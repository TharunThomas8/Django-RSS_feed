from django.shortcuts import render , render_to_response
from . import forms
from . import models
from .models import link
from django.http import HttpResponse
from django.views.generic import ListView
from django.template import loader, Context , RequestContext
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
    		return render_to_response('rss_feed/text.html', {"data": s})
    	except KeyError:
    		return render_to_response('rss_feed/text.html', {"data": "Invalid"})
    else:
        return render_to_response('rss_feed/text.html', {"data": "Empty form"})
    
def get(request):
    template = loader.get_template('rss_feed/list.html')
    link_list = link.objects.all()
    context = RequestContext(request,{'link_list':link_list})
    # print ("...........................")
    # print (link_list)
    # print ("...........................")
    # print (context)
    # print ("...........................")
    return render(request,'rss_feed/list.html',{'link_list':link_list})

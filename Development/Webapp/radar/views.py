from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from radar.models import Speed
# Create your views here.

def index(request):
	last_speed = Speed.objects.order_by('-date_time')[0]
	template = loader.get_template('radar/index.html')
	context = RequestContext(request, {
		'speed': last_speed,
	})
	return HttpResponse(template.render(context))
from django.conf.urls import patterns, url

from radar import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
)
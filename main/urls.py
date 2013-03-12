from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from main import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<id_lugar>\d+)/$', views.detail, name='detail'),
	url(r'^about/',TemplateView.as_view(template_name='main/about.html')),
	url(r'^help/',TemplateView.as_view(template_name='main/help.html'))
)
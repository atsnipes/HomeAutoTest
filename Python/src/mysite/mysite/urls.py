from django.conf.urls import patterns, url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from temp import views


urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^json/$', views.Json_Temp_List, name='Json_Temp_List'),
     url(r'^json/(?P<url_snsr_name>\w+)/$', views.Json_Detail, name='Json_Detail'),
     url(r'^(?P<url_snsr_name>\w+)/$', views.detail, name='detail'),   
#    url(r'^(?P<url_snsr_name>\w+)/$', views.detail, name='detail'),
#    url(r'^(?P<url_snsr_name>\w+)/update/$', views.update_temp, name='update'), 
    
#    url(r'^(?P<url_snsr_name>\w+)/$', views.detail, name='detail'),
#    url(r'^(?P<url_snsr_name>\w+)/rest/$', ),
#    url(r'^(?P<url_snsr_name>\w+)/api_auth/$', include('rest_framework.urls', namespace='rest_framework'))
    
#    url(r'^(?P<snsr_idx>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
#    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
#    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)

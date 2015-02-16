from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
#    url(r'^myapp/', include('myapp.urls', namespace="myapp")),
    url(r'^temp/', include('temp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


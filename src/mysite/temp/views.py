from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django import forms
#for  rest stuff
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

#custom stuff
from temp.models import TempInput
from temp.serializers import TempInputSerializer

import simplejson
#import json as simplejson

#for charting
from chartit import DataPool, Chart

MAX_NUM_VIEW_SNSRS = 10

# Create your views here.
def index(request):
#create list of latest 5 sensor objects
    latest_snsr_list = TempInput.objects.order_by('-snsr_create_date')[:MAX_NUM_VIEW_SNSRS]
    template = loader.get_template('temp/index.html')
    context = { 'latest_snsr_list': latest_snsr_list }  
    return render(request, 'temp/index.html', context)  
  
def detail(request, url_snsr_name):
    sel_snsr = get_object_or_404(TempInput, snsr_name=url_snsr_name)
    #update temp when the page originally loads. javascript will handle updates in template after
  #  sel_snsr.update_temp()
    return render(request, 'temp/detail.html',{'sel_snsr':sel_snsr})

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def Json_Temp_List(request):
    print "TEMP_LIST"
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temp_list = TempInput.objects.all()
        serializer = TempInputSerializer(temp_list, many=True)
        return JSONResponse(serializer.data)
# won't need POST because this will be Read-Only at first
#    elif request.method == 'POST':
#        data = JSONParser().parse(request)
 #       serializer = SnippetSerializer(data=data)
 #       if serializer.is_valid():
 #           serializer.save()
 #           return JSONResponse(serializer.data, status=201)
 #       return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def Json_Detail(request, url_snsr_name):
    print "JSON_DETAIL"
    """
    Retrieve, update or delete a code snippet.
    """
    
    sel_snsr = get_object_or_404(TempInput, snsr_name=url_snsr_name)
    
    if request.method == 'GET':
        serializer = TempInputSerializer(sel_snsr)
        return JSONResponse(serializer.data)

#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = SnippetSerializer(snippet, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JSONResponse(serializer.data)
#        return JSONResponse(serializer.errors, status=400)

#   elif request.method == 'DELETE':
#        snippet.delete()
#        return HttpResponse(status=204)

# Page for charting
def weather_chart_view(request):
    print "im in the main view"

    #Step 1: Create a DataPool with the data we want to retrieve.
    tempData=\
        DataPool(
           series=
            [{'options': {
               'source': TempInput.objects.all()},
              'terms': [
                ('temp_updated_date', lambda d: time.mktime(d.timetuple())),
                'cur_temp']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource=tempData,
            series_options=
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'temp_updated_date': [
                    'cur_temp']
                  }}],
            chart_options=
              {'title': {
                   'text': 'Total Ratings Counts'},
               'xAxis': {
                    'title': {
                       'text': 'Date/Time'}}})#,
            #x_sortf_mapf_mts=(None, lambda i: datetime.fromtimestamp(i).strftime("%D:%M"), False)))
            
    #Step 3: Send the chart object to the template.
    #return render_to_response({'weatherchart': cht})
    return render(request, 'temp/charts.html',{'tempchart': cht})   
    #return render(request, 'temp/detail.html',{'sel_snsr':sel_snsr})

def weather_chart_view_detail(request):
    
    sel_snsr = get_object_or_404(TempInput, snsr_name=url_snsr_name)


    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': sel_snsr},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response({'weatherchart': cht})

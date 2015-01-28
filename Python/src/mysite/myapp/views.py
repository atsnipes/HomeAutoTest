from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import Http404

from temp.models import TempInput

latest_snsr_list={0}

MAX_SUPPORTED_SNSRS = 10

# Create your views here.
def index(request):
#create list of latest 5 sensor objects
#global latest_snsr_list
    latest_snsr_list = TempInput.objects.order_by('-snsr_create_date')[:MAX_SUPPORTED_SNSRS]
    template = loader.get_template('temp/index.html')
    context = { 'latest_snsr_list': latest_snsr_list }
    return render(request, 'temp/index.html', context)

def detail(request, snsr_idx):
   #if snsr_idx out of range throw FoOhFo
    if(int(snsr_idx) >= MAX_SUPPORTED_SNSRS or int(snsr_idx) < 0):
        return HttpResponse("Sensor doesn't exist you stupid whore")
    try:
#        selected_snsr = TempInput.objects.objects.latest('snsr_create_date')
        selected_snsr = latest_snsr_list[snsr_idx]
    except Exception, e:
     #   print str(e)
        raise Http404

    return HttpResponse("The current temperature is " +  str(selected_snsr))


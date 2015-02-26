import time
from celery.task.schedules import crontab  
from celery.decorators import periodic_task  
from datetime import timedelta

from temp.models import TempInput
MAX_NUM_VIEW_SNSRS = 5 #find a global place to put me or env vars

  
# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab  
#@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))  
@periodic_task(run_every=timedelta(seconds=10))
def test():  
    print "Firing temp update"
    snsr_update_list = TempInput.objects.order_by('-snsr_create_date')[:MAX_NUM_VIEW_SNSRS]
    for snsr in snsr_update_list:
        snsr.update_temp()
     #   time.sleep(.5)
    print "Task Fired"
    

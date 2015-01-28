import datetime
import serial
import time
import re
from django.db import models
from django.utils import timezone

#from SerialTempRead import rd_temp
# Create your models here.
class TempInput(models.Model):
    snsr_create_date = models.DateTimeField('Date Created', default=timezone.now())
    snsr_name = models.CharField(max_length=50, default="Def_Snsr")
    cur_temp = models.IntegerField(default=0)
    temp_units = models.CharField(max_length=1, default="F")
    temp_updated_date = models.DateTimeField('Current Temperature Taken at',default=timezone.now())
    
    #temps_list[] then temps_list.append(temp_obj)
    
    def __str__(self):
        return str(self.cur_temp)
    def was_created_recently(self):
        return self.snsr_create_date >= timezone.now() - datetime.timedelta(days=1)
    def set_cur_temp(self,cur_tempin,cur_time):
        self.cur_temp = cur_tempin
        self.temp_updated_date = cur_time
    def set_units(self,units):
        if(units != 'F' and units != 'C'):
            return
        self.temp_units = units
    def read_snsr(self):
        self.rd_temp()

    def rd_temp(self):
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        time.sleep(1)
        ser.flush()
        ser.write("f\n")
        time.sleep(1)
        val = ser.read(ser.inWaiting())
        #temp_list = extract_number(val)
        temp_list = re.findall('[-+]?[0-9]+(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?',val)
        if(temp_list):
            print "Found Floats = "+str(temp_list)
        else:
            print "No floats found"
        ser.close()
        temp = float(temp_list[0])
        return temp
    def update_temp(self):
        temp = self.rd_temp()
        print "tempout = "+str(temp)
        self.set_cur_temp(temp,timezone.now())
        self.save()

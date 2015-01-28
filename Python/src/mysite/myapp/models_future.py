#import datetime

from django.db import models
#from django.utils import timezone

class TempInput(models.Model):
      temp_input = models.CharField(max_length=7)

      def __str__(self):
	return self.temp_input;

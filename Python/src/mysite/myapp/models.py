import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text;
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = s
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text;
    
class TempInput(models.Model):
    snsr_create_date = models.DateTimeField('Date Created', default=timezone.now())
    snsr_name = models.CharField(max_length=50)
    cur_temp = models.IntegerField(default=0)
    temp_taken_date = models.DateTimeField('Current Temperature Taken at')
    
    #temps_list[] then temps_list.append(temp_obj)
    
    def __str__(self):
        return str(self.cur_temp)
    def was_created_recently(self):
        return self.snsr_create_date >= timezone.now() - datetime.timedelta(days=1)
    def set_cur_temp(self,cur_tempin,cur_time):
        self.cur_temp = cur_tempin
        self.temp_taken_date = cur_time
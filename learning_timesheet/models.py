from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Timesheet_Data(models.Model):
    user = models.CharField(null=True, blank= True, max_length = 10)
    #task_done = models.CharField(max_length=10, blank = True)
    date = models.CharField(null=True, blank=True, max_length= 12)
    time_utilised_ws = models.IntegerField(null=True)
    time_utilised_rs = models.IntegerField(null=True)
    time_utilised_rp = models.IntegerField(null=True)
    time_utilised_mt = models.IntegerField(null=True)
    time_utilised_ml = models.IntegerField(null=True)

    def __str__(self):
        return self.date

class KVM_data(models.Model):
    user = models.CharField(null=True, blank= True, max_length = 10)
    month = models.CharField(null=True, blank= True, max_length = 10)
    #ss = datetime.strptime(month,"%Y-%m-%d")
    #abc = month.strftime("%B")
    link_scraped = models.IntegerField(null=True)
    link_resolved = models.IntegerField(null=True)
    days_to_reply = models.IntegerField(null=True)
    average_tat = models.IntegerField(null=True)

    def __str__(self):
        return self.month

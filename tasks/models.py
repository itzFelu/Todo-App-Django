import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    id = models.BigAutoField(primary_key=True)
    title= models.CharField(max_length=100)
    description= models.TextField(max_length=500)
    CHOICE=[
        ('Done', True),
        ('Pending', False),
    ]
    status=models.CharField(max_length=10,choices=CHOICE,default='Pending')
    timeOf_creation=models.DateTimeField(default=datetime.datetime.now())
    timeOf_last_update=models.DateTimeField(default=datetime.datetime.now())

    created_by=models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Activity_log(models.Model):
    log_id=models.BigAutoField(primary_key=True)

    task_id = models.IntegerField(null=True, blank=True)
    title= models.CharField(max_length=100,null=True, blank=True)
    description= models.TextField(max_length=500,null=True, blank=True)
    status=models.CharField(max_length=10,null=True, blank=True)
    timeOf_creation=models.DateTimeField(null=True, blank=True)
    timeOf_last_update=models.DateTimeField(null=True, blank=True)
    performed_by=models.ForeignKey(User,on_delete=models.DO_NOTHING, null=True, blank=True)

    nameOf_action_performed= models.TextField()
    timeOf_action_performed= models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.action_performed
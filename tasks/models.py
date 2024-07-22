from django.db import models
import datetime
# Create your models here.
class Tasks(models.Model):
    title= models.CharField(max_length=100)
    description= models.CharField(max_length=500)
    CHOICE=[
        ('Done', True),
        ('Pending', False),
    ]
    status=models.CharField(max_length=10,choices=CHOICE,default=False)
    dateTime=models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title
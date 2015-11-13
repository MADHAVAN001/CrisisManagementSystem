from django.db import models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrisisManagementSystem.settings")

TYPE=((1, 'FIRE' ),
                    (2, 'FLOOD'),
                    (3, 'MEDICAL EMERGENCY'),
                    (4, 'INDUSTRIAL ACCIDENT'),
                    (5, 'BAD WEATHER'),
                    (6, 'OTHERS')
                )
SEVERITY =(
    (1, 'EXTREMELY URGENT'),
    (2, 'VERY URGENT'),
    (3, 'URGENT'),
    (4, 'LESS URGENT'),
    (5, 'VERY LESS URGENT')
)

class Agency(models.Model):
    name = models.CharField(max_length=50)
    telephone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=50, unique=True)
    type=models.IntegerField()

class Subscriber (models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=8)
    nric = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    postalcode = models.CharField(max_length=6)
    email = models.CharField(max_length=50, unique=True)

class ReportReceiver(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)

class Crisis(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=150, null=True)
    postalcode = models.CharField(max_length=6)
    type = models.IntegerField()
    severity=models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    personName = models.CharField(max_length=30)
    personPhone = models.CharField(max_length=8)
    isActive = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
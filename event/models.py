from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager
from spot.models import Place
# Create your models here.

class Event(TimeStampedModel):
    title = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True)
    tags = TaggableManager()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title} at {self.place}'
    
class Timing(models.Model):
    event_date = models.DateField(null=True, blank=True)
    event_time = models.TimeField(null=True, blank=True)
    event = models.ForeignKey('Event',on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.event} - {self.event_date} - {self.event_time}'
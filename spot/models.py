from django.db import models
from django.contrib.gis.db.models import PointField
from django.urls import reverse
# Create your models here.

class Place(models.Model):
    title = models.CharField(max_length=200, null=True)
    location = PointField(null=True, blank=True)
    description = models.TextField(max_length=2000, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(max_length=200, null=True)
    type_of_place = models.CharField(max_length=200, null=True)
    tags = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular place."""
        return reverse('spot:detail-place', args=[str(self.id)])

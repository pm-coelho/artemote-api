from django.db import models
from django.contrib.gis.db.models import PointField


class Address(models.Model):
    city = models.CharField(max_length=100, blank=True, null=True)
    city_district = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=100, blank=True, null=True)
    suburb = models.CharField(max_length=100, blank=True, null=True)

    location = PointField(blank=True, null=True)

    class Meta:
        default_related_name = "addresses"

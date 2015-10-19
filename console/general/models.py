from django.db import models
from console.login.models import Variant


class Dimensions(models.Model):
    class Meta:
        db_table = 'dimensions'

    variant = models.ForeignKey(Variant)
    length = models.CharField(max_length=100, blank=False)
    width = models.CharField(max_length=100, blank=False)
    height = models.CharField(max_length=100, blank=False)
    wheelbase = models.CharField(max_length=100, blank=True, null=True)
    bootspace = models.CharField(max_length=100, blank=True, null=True)
    kerbweight = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Brake(models.Model):
    class Meta:
        db_table = 'brakes'

    variant = models.ForeignKey(Variant)
    rear_brakes = models.CharField(max_length=100, blank=False)
    front_brakes = models.CharField(max_length=100, blank=False)


class Capacity(models.Model):
    class Meta:
        db_table = 'capacity'

    variant = models.ForeignKey(Variant)
    seating_capacity = models.PositiveIntegerField(null=True)
    tank_capacity = models.CharField(max_length=100, blank=True, null=True)


class Mileage(models.Model):
    class Meta:
        db_table = 'mileage'

    variant = models.ForeignKey(Variant)
    mileage_highway = models.CharField(max_length=100, blank=True, null=True)
    mileage_city = models.CharField(max_length=100, blank=True, null=True)
    mileage_overall = models.CharField(max_length=100, blank=True, null=True)

class Price(models.Model):
    class Meta:
        db_table = 'price'

    variant = models.ForeignKey(Variant)
    showroom_price=models.CharField(max_length=100, blank=True, null=True)
    onroad_price  =models.CharField(max_length=100, blank=True, null=True)

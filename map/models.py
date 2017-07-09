# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from neomodel import StructuredNode, StringProperty, Relationship


# from neo4django.db import models as neo_models


class Blocks(models.Model):
    startipnum = models.AutoField(db_column='startIpNum', primary_key=True)
    endipnum = models.IntegerField(
        db_column='endIpNum', blank=True, null=True)
    locid = models.IntegerField(db_column='locId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blocks'


class Location(models.Model):
    locid = models.AutoField(db_column='locId', primary_key=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    region = models.CharField(max_length=2, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    postalcode = models.CharField(
        db_column='postalCode', max_length=10, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    metrocode = models.IntegerField(
        db_column='metroCode', blank=True, null=True)
    areacode = models.IntegerField(db_column='areaCode', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Router(StructuredNode):
    ip = StringProperty()
    country = StringProperty()
    city = StringProperty()

    router_re = Relationship('Router', 'IS_FROM')

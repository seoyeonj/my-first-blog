# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AiriotTable(models.Model):
    index = models.AutoField(primary_key=True)
    userid = models.CharField(db_column='userID', max_length=100)  # Field name made lowercase.
    device = models.CharField(max_length=100)
    day = models.CharField(max_length=200)
    time = models.CharField(max_length=100)
    voc_volts = models.IntegerField()
    co2_volts = models.IntegerField()
    gas_volts = models.IntegerField()
    pm25 = models.IntegerField()
    pm10 = models.IntegerField()
    pm01 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'AirIoT_table'


class AirqualityTable(models.Model):
    index = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    so2 = models.FloatField()
    co = models.FloatField()
    o3 = models.FloatField()
    no2 = models.FloatField()
    pm10 = models.FloatField()
    pm25 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'airquality_table'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SmartthingsTable(models.Model):
    index = models.AutoField(primary_key=True)
    userid = models.CharField(db_column='UserID', max_length=100)  # Field name made lowercase.
    device = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    device_value = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'smartthings_table'



class WayskinTable(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userID', max_length=100)  # Field name made lowercase.
    device = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    skin_moisture = models.IntegerField()
    part = models.CharField(max_length=100)
    m_char = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'wayskin_table'


class WeatherTable(models.Model):
    index = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    wind_wdir = models.IntegerField()
    wind_wspd = models.IntegerField()
    precipitation = models.IntegerField()
    sky = models.CharField(max_length=100)
    temperature = models.IntegerField()
    humidity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weather_table'

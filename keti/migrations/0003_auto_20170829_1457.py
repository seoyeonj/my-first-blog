# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 05:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keti', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserTable',
        ),
    ]

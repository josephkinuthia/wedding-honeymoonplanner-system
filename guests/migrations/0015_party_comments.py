# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-04 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0014_auto_20160326_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
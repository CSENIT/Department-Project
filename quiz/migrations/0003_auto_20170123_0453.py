# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20170123_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz_data',
            name='quiz_image',
            field=models.ImageField(blank=True, max_length=512, upload_to='media/quiz_image/'),
        ),
    ]

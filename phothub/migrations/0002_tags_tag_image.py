# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phothub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='tag_image',
            field=models.ImageField(default=1, upload_to='tags/'),
            preserve_default=False,
        ),
    ]

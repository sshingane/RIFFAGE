# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_auto_20171101_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='riff',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=b'riff_documents/'),
        ),
        migrations.AlterField(
            model_name='riff',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=b'riff_audio/'),
        ),
    ]

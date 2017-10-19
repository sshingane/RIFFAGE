# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20171018_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riff',
            name='riff_key',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('Ab', 'Ab'), ('Bb', 'Bb'), ('Db', 'Db'), ('Eb', 'Eb'), ('Gb', 'Gb')], default='A', max_length=2),
        ),
        migrations.AlterField(
            model_name='riff',
            name='timesig_denom',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (4, '4'), (8, '8'), (16, '16'), (32, '32')], default=4),
        ),
    ]

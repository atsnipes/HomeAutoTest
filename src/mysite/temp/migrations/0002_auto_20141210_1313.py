# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempinput',
            name='snsr_create_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 19, 13, 13, 563599, tzinfo=utc), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tempinput',
            name='snsr_name',
            field=models.CharField(default=b'Def_Snsr', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tempinput',
            name='temp_taken_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 19, 13, 13, 565673, tzinfo=utc), verbose_name=b'Current Temperature Taken at'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0006_auto_20141210_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempinput',
            name='temp_units',
            field=models.CharField(default=b'F', max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tempinput',
            name='snsr_create_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 12, 22, 17, 14, 326094, tzinfo=utc), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tempinput',
            name='temp_taken_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 12, 22, 17, 14, 329178, tzinfo=utc), verbose_name=b'Current Temperature Taken at'),
            preserve_default=True,
        ),
    ]

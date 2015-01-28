# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0004_auto_20141210_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempinput',
            name='snsr_create_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 19, 24, 51, 584103, tzinfo=utc), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tempinput',
            name='temp_taken_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 19, 24, 51, 586189, tzinfo=utc), verbose_name=b'Current Temperature Taken at'),
            preserve_default=True,
        ),
    ]

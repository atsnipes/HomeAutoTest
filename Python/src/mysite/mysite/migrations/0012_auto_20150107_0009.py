# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0011_auto_20150104_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempinput',
            name='snsr_create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 7, 6, 8, 57, 961753, tzinfo=utc), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tempinput',
            name='temp_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 7, 6, 8, 57, 967066, tzinfo=utc), verbose_name=b'Current Temperature Taken at'),
            preserve_default=True,
        ),
    ]

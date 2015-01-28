# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0007_auto_20141212_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempinput',
            name='temp_taken_date',
        ),
        migrations.AddField(
            model_name='tempinput',
            name='temp_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 12, 22, 26, 49, 281436, tzinfo=utc), verbose_name=b'Current Temperature Taken at'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tempinput',
            name='snsr_create_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 12, 22, 26, 49, 268420, tzinfo=utc), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
    ]

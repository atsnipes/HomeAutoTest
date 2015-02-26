# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0014_auto_20150216_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempinput',
            name='snsr_create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 17, 3, 41, 59, 356949, tzinfo=utc), verbose_name=b'Date Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tempinput',
            name='temp_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 17, 3, 41, 59, 362731, tzinfo=utc), verbose_name=b'Current Temperature Taken at'),
            preserve_default=True,
        ),
    ]

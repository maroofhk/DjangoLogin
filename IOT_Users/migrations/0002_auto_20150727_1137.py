# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IOT_Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iotuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='iotuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='iotuser',
            name='last_name',
        ),
    ]

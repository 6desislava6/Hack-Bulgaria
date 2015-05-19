# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150519_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover',
            field=models.ImageField(upload_to='', default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

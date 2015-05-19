# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_projection', models.CharField(max_length=6)),
                ('date', models.DateField()),
                ('time_projection', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('projection', models.ForeignKey(to='website.Projection')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='length',
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='projection',
            name='movie',
            field=models.ForeignKey(to='website.Movie'),
        ),
    ]

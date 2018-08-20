# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='families',
            name='Address',
            field=models.CharField(verbose_name='Address', blank=True, db_column='Address', null=True, max_length=254),
        ),
        migrations.AddField(
            model_name='families',
            name='City',
            field=models.CharField(verbose_name='City', blank=True, db_column='City', null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='families',
            name='State',
            field=models.CharField(verbose_name='State', blank=True, db_column='State', null=True, max_length=2),
        ),
        migrations.AddField(
            model_name='families',
            name='Zip',
            field=models.CharField(verbose_name='Zip', blank=True, db_column='Zip', null=True, max_length=10),
        ),
    ]

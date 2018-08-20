# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151005_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='families',
            name='Phone',
            field=models.CharField(verbose_name='Phone', null=True, max_length=25, blank=True, db_column='Phone'),
        ),
    ]

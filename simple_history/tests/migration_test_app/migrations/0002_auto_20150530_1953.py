# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('migration_test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalyar',
            name='what',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='migration_test_app.WhatIMean', null=True),
        ),
    ]

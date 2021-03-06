# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0002_auto_20160923_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('pokee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokee', to='loginreg.User')),
                ('poker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poker', to='loginreg.User')),
            ],
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]

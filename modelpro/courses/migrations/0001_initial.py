# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-06-28 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('rollno', models.IntegerField()),
                ('addr', models.CharField(max_length=100)),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-06 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('emp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multilevelapp.Emp')),
                ('sname', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
            ],
            bases=('multilevelapp.emp',),
        ),
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('student_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multilevelapp.Student')),
                ('cname', models.CharField(max_length=100)),
                ('sales', models.IntegerField()),
            ],
            bases=('multilevelapp.student',),
        ),
    ]

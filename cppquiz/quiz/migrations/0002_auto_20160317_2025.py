# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-17 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='result',
            field=models.CharField(choices=[(b'OK', b'The program is guaranteed to output'), (b'CE', b'The program has a compilation error'), (b'US', b'The program is unspecified / implementation defined'), (b'UD', b'The program is undefined')], default=b'OK', max_length=2),
        ),
        migrations.AlterField(
            model_name='usersanswer',
            name='result',
            field=models.CharField(choices=[(b'OK', b'The program is guaranteed to output'), (b'CE', b'The program has a compilation error'), (b'US', b'The program is unspecified / implementation defined'), (b'UD', b'The program is undefined')], default=b'OK', max_length=2),
        ),
    ]

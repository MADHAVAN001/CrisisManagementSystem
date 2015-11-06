# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(unique=True, max_length=50)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Crisis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=150, null=True)),
                ('postalcode', models.CharField(max_length=6)),
                ('type', models.IntegerField()),
                ('severity', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('personName', models.CharField(max_length=30)),
                ('personPhone', models.CharField(max_length=8)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportReceiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=8)),
                ('nric', models.CharField(unique=True, max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('postalcode', models.CharField(max_length=6)),
                ('email', models.CharField(unique=True, max_length=50)),
            ],
        ),
    ]

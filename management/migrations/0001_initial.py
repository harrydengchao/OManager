# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('module_name', models.CharField(max_length=60)),
                ('module_caption', models.CharField(max_length=800)),
                ('module_extend', models.CharField(max_length=6000)),
                ('delmark', models.CharField(default=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ServerAppCateg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fun_categ_id', models.IntegerField()),
                ('app_categ_name', models.CharField(max_length=90)),
                ('delmark', models.CharField(default=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ServerFunCateg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_categ_name', models.CharField(max_length=60)),
                ('delmark', models.CharField(default=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ServerHostList',
            fields=[
                ('app_categ_id', models.IntegerField()),
                ('host_name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('host_wip', models.CharField(max_length=50)),
                ('host_nip', models.CharField(max_length=50)),
                ('host_os', models.CharField(max_length=30)),
                ('delmark', models.CharField(default=False, max_length=10)),
            ],
        ),
    ]

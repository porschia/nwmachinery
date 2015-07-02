# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCapture',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.TextField(default='')),
                ('email', models.EmailField(max_length=75)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

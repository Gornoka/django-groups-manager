# Generated by Django 2.2.8 on 2019-12-10 11:37

import collections
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('groups_manager', '0005_0_6_2_verbose_name_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='django_auth_sync',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='properties',
            field=jsonfield.fields.JSONField(blank=True, default={}, load_kwargs={'object_pairs_hook': collections.OrderedDict}, verbose_name='properties'),
        ),
        migrations.AlterField(
            model_name='group',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='django_auth_sync',
            field=models.BooleanField(blank=True, default=True, verbose_name='django auth sync'),
        ),
    ]
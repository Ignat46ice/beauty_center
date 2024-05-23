# Generated by Django 5.0.6 on 2024-05-23 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_remove_service_stylists_service_stylists'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='stylists',
        ),
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

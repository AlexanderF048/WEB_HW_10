# Generated by Django 4.1.6 on 2023-02-06 22:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=15), size=15),
        ),
    ]

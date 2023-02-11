# Generated by Django 4.1.6 on 2023-02-11 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_quotes', '0003_authors_user_quotes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='born_date',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='authors',
            name='born_location',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='authors',
            name='description',
            field=models.CharField(default=None, max_length=5000),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_quotes.authors'),
        ),
    ]

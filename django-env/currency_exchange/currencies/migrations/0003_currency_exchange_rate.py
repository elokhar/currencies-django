# Generated by Django 5.1.3 on 2024-11-21 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_currency_reverse_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='exchange_rate',
            field=models.FloatField(default=0),
        ),
    ]

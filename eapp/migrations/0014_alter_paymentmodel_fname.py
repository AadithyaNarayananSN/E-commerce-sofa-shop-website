# Generated by Django 4.1.5 on 2023-02-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0013_paymentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='fname',
            field=models.CharField(max_length=50),
        ),
    ]

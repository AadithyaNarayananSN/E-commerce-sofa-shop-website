# Generated by Django 4.1.5 on 2023-01-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0005_productmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.FileField(upload_to='eapp/static'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-26 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0006_alter_productmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='desc',
        ),
    ]
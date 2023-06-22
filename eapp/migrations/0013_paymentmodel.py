# Generated by Django 4.1.5 on 2023-02-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0012_buymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('paymode', models.CharField(max_length=50)),
            ],
        ),
    ]

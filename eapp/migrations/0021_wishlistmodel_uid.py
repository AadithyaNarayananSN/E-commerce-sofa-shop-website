# Generated by Django 4.1.5 on 2023-02-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0020_paymentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistmodel',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

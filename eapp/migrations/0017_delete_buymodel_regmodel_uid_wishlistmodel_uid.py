# Generated by Django 4.1.5 on 2023-02-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0016_paymentmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='buymodel',
        ),
        migrations.AddField(
            model_name='regmodel',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlistmodel',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
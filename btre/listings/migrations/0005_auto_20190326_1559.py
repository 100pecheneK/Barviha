# Generated by Django 2.1.7 on 2019-03-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20190326_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]

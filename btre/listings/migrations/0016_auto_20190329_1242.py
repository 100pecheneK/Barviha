# Generated by Django 2.1.7 on 2019-03-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_auto_20190328_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Улица'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0006_auto_20190324_0708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'Район', 'verbose_name_plural': 'Районы'},
        ),
        migrations.AlterModelOptions(
            name='rent',
            options={'verbose_name': 'Аренду', 'verbose_name_plural': 'Аренды'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Квартиру', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterField(
            model_name='rent',
            name='image',
            field=models.ImageField(default='', upload_to='adminsite/static/adminsite/images/rent', verbose_name='фото квартиры'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(default='', upload_to='adminsite/static/adminsite/images/room', verbose_name='фото квартиры'),
        ),
    ]
# Generated by Django 2.1.7 on 2019-03-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_main', '0002_auto_20190301_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('text', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20190603_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disability',
            name='disability',
            field=models.CharField(default='1', max_length=30),
        ),
        migrations.AlterField(
            model_name='language',
            name='dialect',
            field=models.CharField(default='1', max_length=30),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20190603_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='disability',
            field=models.ManyToManyField(blank=True, null=True, to='users.Disability'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.ManyToManyField(blank=True, null=True, to='users.Language'),
        ),
    ]

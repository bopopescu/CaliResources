# Generated by Django 2.2.1 on 2019-06-03 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20190603_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disability',
            name='user',
        ),
        migrations.RemoveField(
            model_name='language',
            name='user',
        ),
        migrations.AlterField(
            model_name='disability',
            name='disability',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_disability',
            field=models.ManyToManyField(blank=True, to='users.Disability'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_language',
            field=models.ManyToManyField(blank=True, to='users.Language'),
        ),
    ]
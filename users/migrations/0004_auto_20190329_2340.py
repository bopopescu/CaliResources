# Generated by Django 2.1.7 on 2019-03-29 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190326_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', upload_to='profile_pics'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_feed', '0002_auto_20180616_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='links',
        ),
    ]
# Generated by Django 2.2.6 on 2019-10-14 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='author',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='date_posted',
        ),
    ]
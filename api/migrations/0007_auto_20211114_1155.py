# Generated by Django 3.1.5 on 2021-11-14 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211114_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='date',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='text1',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='text3',
        ),
    ]

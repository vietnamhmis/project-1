# Generated by Django 2.2 on 2022-12-07 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0003_auto_20221207_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='danhgia_nluc',
            name='user',
        ),
    ]

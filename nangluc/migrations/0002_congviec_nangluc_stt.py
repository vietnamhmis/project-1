# Generated by Django 2.2 on 2022-12-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='congviec_nangluc',
            name='stt',
            field=models.IntegerField(default=2),
        ),
    ]

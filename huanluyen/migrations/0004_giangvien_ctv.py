# Generated by Django 2.2 on 2022-11-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huanluyen', '0003_auto_20221130_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='giangvien',
            name='CTV',
            field=models.BooleanField(default=True),
        ),
    ]

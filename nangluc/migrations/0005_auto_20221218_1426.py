# Generated by Django 2.2 on 2022-12-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0004_auto_20221218_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tong_nl',
            name='Ketqua_danhgia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

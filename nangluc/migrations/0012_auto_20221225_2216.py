# Generated by Django 2.2 on 2022-12-25 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0011_auto_20221225_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='congviec_nangluc',
            options={'ordering': ['chucdanh_CV', 'stt', 'nangluc_cv', 'name']},
        ),
    ]

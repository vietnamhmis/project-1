# Generated by Django 2.2 on 2022-11-29 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhansu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nang_luc_2',
            options={'ordering': ['loai_nang_luc', 'ma_nangluc']},
        ),
    ]
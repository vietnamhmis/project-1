# Generated by Django 2.2 on 2023-01-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhansu', '0008_auto_20230107_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpi_list',
            name='Su_dung',
            field=models.BooleanField(default=False),
        ),
    ]
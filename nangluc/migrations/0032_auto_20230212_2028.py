# Generated by Django 2.2 on 2023-02-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0031_auto_20230212_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='tu_danhgia_dapung',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
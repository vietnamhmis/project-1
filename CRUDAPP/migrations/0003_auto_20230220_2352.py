# Generated by Django 2.2 on 2023-02-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDAPP', '0002_auto_20230217_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]

# Generated by Django 2.2 on 2023-02-24 15:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDAPP', '0003_auto_20230220_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='gender',
            field=models.CharField(default=datetime.datetime(2023, 2, 24, 15, 39, 37, 204213, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]

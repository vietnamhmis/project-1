# Generated by Django 2.2 on 2023-02-12 14:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0033_auto_20230212_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='TenNangluc_congviec',
            field=models.CharField(default=datetime.datetime(2023, 2, 12, 14, 14, 46, 93109, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]

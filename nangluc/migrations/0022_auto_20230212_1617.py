# Generated by Django 2.2 on 2023-02-12 09:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0021_danhgia_nluc_thu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='danhgia_nluc_thu',
            name='Ketqua_danhgia',
        ),
        migrations.RemoveField(
            model_name='danhgia_nluc_thu',
            name='start_date',
        ),
        migrations.AddField(
            model_name='danhgia_nluc_thu',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 2, 12, 9, 17, 37, 906606, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='danhgia_nluc_thu',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

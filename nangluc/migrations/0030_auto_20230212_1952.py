# Generated by Django 2.2 on 2023-02-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nangluc', '0029_auto_20230212_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
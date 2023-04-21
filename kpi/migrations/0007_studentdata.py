# Generated by Django 2.2 on 2023-02-11 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0006_delete_studentdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

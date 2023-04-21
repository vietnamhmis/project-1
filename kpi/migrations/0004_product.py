# Generated by Django 2.2 on 2023-02-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0003_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dateadded', models.DateField(blank=True, null=True)),
                ('productcode', models.CharField(blank=True, max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('category_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pillow'), (2, 'Food'), (3, 'Toys')], null=True)),
            ],
            options={
                'db_table': 'myapp_product',
            },
        ),
    ]

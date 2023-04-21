# Generated by Django 2.2 on 2022-11-20 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='giangvien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Lopdaotao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Noidungdaotao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('ngay_daotao', models.DateField(blank=True, null=True)),
                ('educator', models.TextField(blank=True, max_length=50, null=True)),
                ('excerpt', models.TextField(blank=True, max_length=500, null=True)),
                ('number_lessons', models.PositiveSmallIntegerField(default=1)),
                ('tenlop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dao_tao.Lopdaotao')),
            ],
        ),
    ]

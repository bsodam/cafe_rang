# Generated by Django 2.1.5 on 2019-01-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe_name', models.CharField(max_length=30)),
                ('cafe_address', models.CharField(max_length=100)),
                ('cafe_phone', models.CharField(max_length=30)),
                ('cafe_opening_hours', models.CharField(blank=True, max_length=100)),
                ('cafe_menu', models.TextField(blank=True)),
            ],
        ),
    ]

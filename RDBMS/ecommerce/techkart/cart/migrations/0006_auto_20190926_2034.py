# Generated by Django 2.2.3 on 2019-09-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20190926_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingorder',
            name='quantity',
            field=models.CharField(max_length=20),
        ),
    ]

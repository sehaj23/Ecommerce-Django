# Generated by Django 2.2.3 on 2019-09-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_pendingorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingorder',
            name='cid',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pendingorder',
            name='pid',
            field=models.IntegerField(max_length=20),
        ),
    ]

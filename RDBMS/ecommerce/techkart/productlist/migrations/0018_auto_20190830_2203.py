# Generated by Django 2.2.3 on 2019-08-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0017_hotdeals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotdeals',
            name='description',
            field=models.TextField(max_length=400),
        ),
    ]

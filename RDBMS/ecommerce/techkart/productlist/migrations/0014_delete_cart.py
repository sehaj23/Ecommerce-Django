# Generated by Django 2.2.3 on 2019-08-23 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0013_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cart',
        ),
    ]

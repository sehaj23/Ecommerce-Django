# Generated by Django 2.2.3 on 2019-08-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0003_auto_20190818_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='p_specification',
            field=models.TextField(default=0, max_length=400),
            preserve_default=False,
        ),
    ]
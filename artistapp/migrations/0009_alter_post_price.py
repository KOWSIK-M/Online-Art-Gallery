# Generated by Django 4.2.5 on 2023-11-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistapp', '0008_cartitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=1000),
        ),
    ]
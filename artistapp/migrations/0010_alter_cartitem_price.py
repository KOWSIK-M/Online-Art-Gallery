# Generated by Django 4.2.5 on 2023-11-04 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistapp', '0009_alter_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=1000),
        ),
    ]

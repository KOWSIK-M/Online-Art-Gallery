# Generated by Django 4.2.5 on 2023-11-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistapp', '0010_alter_cartitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(default='static/user_profiles/userpic.png', upload_to='posts/'),
        ),
    ]
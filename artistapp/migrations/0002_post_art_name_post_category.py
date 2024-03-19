# Generated by Django 4.2.5 on 2023-11-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='art_name',
            field=models.CharField(default='category', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Aesthetic drawings', 'Aesthetic drawings'), ('Traditional Arts', 'Traditional Arts'), ('Sculptures Arts', 'Sculptures Arts'), ('Anime/Manga Arts', 'Anime/Manga Arts'), ('Real life Drawings', 'Real life Drawings'), ('Doodle Art', 'Doodle Art'), ('Pen Drawings', 'Pen Drawings'), ('Nature Arts', 'Nature Arts')], default='Aesthetic', max_length=100),
            preserve_default=False,
        ),
    ]

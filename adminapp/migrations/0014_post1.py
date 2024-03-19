# Generated by Django 4.2.5 on 2023-11-04 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artistapp', '0004_alter_post_caption'),
        ('adminapp', '0013_alter_user_mobilenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Aesthetic drawings', 'Aesthetic drawings'), ('Traditional Arts', 'Traditional Arts'), ('Sculptures Arts', 'Sculptures Arts'), ('Anime/Manga Arts', 'Anime/Manga Arts'), ('Real life Drawings', 'Real life Drawings'), ('Doodle Art', 'Doodle Art'), ('Pen Drawings', 'Pen Drawings'), ('Nature Arts', 'Nature Arts')], max_length=100)),
                ('image', models.ImageField(upload_to='posts/')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistapp.artist')),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_posts', to='adminapp.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.user')),
            ],
            options={
                'db_table': 'post_table1',
            },
        ),
    ]

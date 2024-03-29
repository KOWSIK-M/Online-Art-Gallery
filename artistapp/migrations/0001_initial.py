# Generated by Django 4.2.5 on 2023-10-26 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('FullName', models.CharField(max_length=100)),
                ('DateOfBirth', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'O')], max_length=10)),
                ('Username', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('MobileNumber', models.CharField(max_length=20, unique=True)),
                ('Email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('TypeOfArtist', models.CharField(choices=[('Aesthetic drawings', 'Aesthetic drawings'), ('Traditional Arts', 'Traditional Arts'), ('Sculptures Arts', 'Sculptures Arts'), ('Anime/Manga Arts', 'Anime/Manga Arts'), ('Real life Drawings', 'Real life Drawings'), ('Doodle Art', 'Doodle Art'), ('Pen Drawings', 'Pen Drawings'), ('Nature Arts', 'Nature Arts')], max_length=100)),
            ],
            options={
                'db_table': 'artist_table',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/')),
                ('caption', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistapp.artist')),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'post_table',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistapp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistProfile',
            fields=[
                ('username', models.CharField(default='user2086', max_length=100, primary_key=True, serialize=False, unique=True)),
                ('artist_pic', models.ImageField(default='static/user_profiles/userpic.png', upload_to='artist_pics/')),
                ('bio', models.TextField(default='Add Bio✏️')),
                ('social_media', models.CharField(blank=True, max_length=100)),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='artistapp.artist')),
            ],
            options={
                'db_table': 'artistprofile_table',
            },
        ),
    ]

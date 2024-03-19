# Generated by Django 4.2.5 on 2023-11-04 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artistapp', '0004_alter_post_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('FullName', models.CharField(max_length=100)),
                ('DateOfBirth', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'O')], max_length=10)),
                ('Username', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('MobileNumber', models.CharField(max_length=10, unique=True)),
                ('Email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(default='user2086', max_length=100, primary_key=True, serialize=False, unique=True)),
                ('user_pic', models.ImageField(default='static/user_profiles/userpic.png', upload_to='user_pics/')),
                ('bio', models.TextField(default='Add Bio✏️')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='artistapp.user')),
            ],
            options={
                'db_table': 'profile_table',
            },
        ),
    ]
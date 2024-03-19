# Generated by Django 4.2.5 on 2023-10-22 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_alter_user_user_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_pic',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pic', models.ImageField(default='static/user_profiles/userpic.png', upload_to='user_pics/')),
                ('bio', models.TextField(default='Add Bio✏️')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.user')),
            ],
        ),
    ]

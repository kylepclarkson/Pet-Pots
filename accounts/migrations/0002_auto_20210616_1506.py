# Generated by Django 3.2.4 on 2021-06-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='account/account_avatar_512_512.jpg', upload_to='account/avatar/'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]

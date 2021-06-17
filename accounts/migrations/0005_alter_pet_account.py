# Generated by Django 3.2.4 on 2021-06-17 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_pet_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet', to='accounts.account'),
        ),
    ]

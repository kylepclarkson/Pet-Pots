# Generated by Django 3.2.4 on 2021-06-17 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20210617_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pets', models.ManyToManyField(to='accounts.Pet')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
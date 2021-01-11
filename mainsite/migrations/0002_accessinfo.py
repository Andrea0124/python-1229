# Generated by Django 3.1.2 on 2020-12-01 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-access_time',),
            },
        ),
    ]

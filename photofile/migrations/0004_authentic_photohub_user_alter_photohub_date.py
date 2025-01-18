# Generated by Django 5.1.4 on 2025-01-18 04:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photofile', '0003_remove_photohub_time_photohub_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('first_name', models.CharField(default='Alice', max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(default='carter', max_length=100, verbose_name='Last Name')),
            ],
        ),
        migrations.AddField(
            model_name='photohub',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photohub',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

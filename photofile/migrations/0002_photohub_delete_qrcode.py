# Generated by Django 5.1.4 on 2025-01-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='photohub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='media/')),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Qrcode',
        ),
    ]

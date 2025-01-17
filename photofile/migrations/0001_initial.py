# Generated by Django 5.1 on 2024-12-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='https://example.com', max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='qrcodes/')),
                ('text', models.TextField(default='write here', max_length=500)),
            ],
        ),
    ]

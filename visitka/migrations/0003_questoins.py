# Generated by Django 5.1.4 on 2025-01-22 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitka', '0002_service_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questoins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('question', models.CharField(max_length=150)),
            ],
        ),
    ]

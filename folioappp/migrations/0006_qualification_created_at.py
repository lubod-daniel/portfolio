# Generated by Django 4.2.2 on 2023-08-29 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('folioappp', '0005_dev_employment'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
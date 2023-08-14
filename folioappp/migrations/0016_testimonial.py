# Generated by Django 4.2.2 on 2023-07-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folioappp', '0015_visitormessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]

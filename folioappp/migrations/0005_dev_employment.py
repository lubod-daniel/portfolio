# Generated by Django 4.2.2 on 2023-08-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folioappp', '0004_alter_more_image_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='dev_employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('start_date', models.CharField(blank=True, max_length=50, null=True)),
                ('end_date', models.CharField(blank=True, max_length=50, null=True)),
                ('employer', models.CharField(blank=True, max_length=100, null=True)),
                ('employer_address', models.CharField(max_length=200, null=True)),
                ('responsibility', models.ManyToManyField(to='folioappp.responsibility')),
            ],
        ),
    ]

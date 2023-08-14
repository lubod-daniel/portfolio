# Generated by Django 4.2.2 on 2023-06-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('current', models.CharField(max_length=50, null=True)),
                ('employer', models.CharField(max_length=100, null=True)),
                ('employer_address', models.CharField(max_length=200, null=True)),
                ('responsibility', models.TextField()),
            ],
        ),
<<<<<<< HEAD
=======
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='images')),
                ('img1', models.ImageField(null=True, upload_to='images')),
                ('img2', models.ImageField(null=True, upload_to='images')),
                ('img3', models.ImageField(null=True, upload_to='images')),
            ],
        ),
>>>>>>> origin/master

        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bag', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('still_studying', models.CharField(max_length=50, null=True)),
                ('institution', models.CharField(max_length=100)),
                ('about', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folioappp', '0012_alter_skill_skill_acquired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional_course',
            name='skill',
            field=models.ManyToManyField(null=True, to='folioappp.skill'),
        ),
    ]

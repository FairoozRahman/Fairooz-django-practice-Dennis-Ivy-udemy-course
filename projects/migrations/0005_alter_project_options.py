# Generated by Django 4.2.1 on 2023-06-14 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
    ]
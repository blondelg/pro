# Generated by Django 2.2.11 on 2020-06-21 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogCategory',
            new_name='BlogPageCategory',
        ),
    ]

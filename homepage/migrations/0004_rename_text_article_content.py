# Generated by Django 4.2.6 on 2023-10-16 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_rename_headline_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='text',
            new_name='content',
        ),
    ]
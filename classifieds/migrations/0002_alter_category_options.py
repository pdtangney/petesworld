# Generated by Django 4.2.6 on 2023-10-20 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]

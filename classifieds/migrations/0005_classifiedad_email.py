# Generated by Django 4.2.6 on 2023-10-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0004_remove_classifiedad_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='classifiedad',
            name='email',
            field=models.EmailField(default=-1, max_length=254),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='classifiedad',
            name='email',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
    ]

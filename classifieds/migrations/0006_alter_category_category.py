# Generated by Django 4.2.6 on 2023-10-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0005_classifiedad_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]

# Generated by Django 4.2.8 on 2024-01-21 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
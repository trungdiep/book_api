# Generated by Django 3.2.4 on 2021-06-28 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='year_pubished',
            new_name='year_published',
        ),
    ]
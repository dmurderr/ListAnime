# Generated by Django 3.1.4 on 2020-12-07 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Animes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='author',
            new_name='autor',
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-13 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucket_list', '0006_auto_20201213_0802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='author',
            new_name='user',
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-15 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='full_name',
            new_name='name',
        ),
    ]

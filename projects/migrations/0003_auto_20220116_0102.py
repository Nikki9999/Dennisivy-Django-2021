# Generated by Django 3.0.8 on 2022-01-15 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220116_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Value',
            new_name='value',
        ),
    ]

# Generated by Django 2.0.1 on 2018-05-04 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meituan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='dish',
        ),
    ]

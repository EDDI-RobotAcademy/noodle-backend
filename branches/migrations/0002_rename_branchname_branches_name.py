# Generated by Django 5.1.1 on 2024-09-25 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branches',
            old_name='branchname',
            new_name='name',
        ),
    ]
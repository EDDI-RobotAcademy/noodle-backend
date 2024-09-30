# Generated by Django 5.1.1 on 2024-09-25 03:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('branchname', models.CharField(max_length=64)),
                ('repos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repos.repos')),
            ],
            options={
                'db_table': 'branches',
            },
        ),
    ]
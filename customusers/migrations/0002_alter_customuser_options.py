# Generated by Django 4.1.2 on 2022-11-05 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]

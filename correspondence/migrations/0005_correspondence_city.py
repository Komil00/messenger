# Generated by Django 4.1.2 on 2022-11-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correspondence', '0004_alter_correspondence_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='correspondence',
            name='city',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
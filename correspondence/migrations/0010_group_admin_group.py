# Generated by Django 4.1.2 on 2022-11-09 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('correspondence', '0009_remove_groupcorrespondence_groupname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='admin_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='group_admin', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-05 10:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Correspondence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images_uploaded')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('send_data', models.DateTimeField(auto_now_add=True)),
                ('from_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_author', to=settings.AUTH_USER_MODEL)),
                ('to_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

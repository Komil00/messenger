# Generated by Django 4.1.2 on 2022-11-08 12:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('correspondence', '0007_remove_correspondence_voice_correspondence_textfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupCorrespondence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=40)),
                ('text', models.TextField(blank=True, null=True)),
                ('textfile', models.FileField(blank=True, null=True, upload_to='textfile_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls'])])),
                ('img', models.ImageField(blank=True, null=True, upload_to='images_uploaded')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('send_data', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('groupuser', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

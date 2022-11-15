from django.core.validators import FileExtensionValidator
from django.db import models

from customusers.models import CustomUser


# Create your models here.

class Correspondence(models.Model):
    from_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from_author')
    to_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='to_author')
    text = models.TextField(null=True, blank=True)
    textfile = models.FileField(upload_to='textfile_uploaded', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls'])])
    img = models.ImageField(upload_to='images_uploaded', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    send_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_author}' + " -> " + f'{self.to_author}'


class Group(models.Model):
    name = models.CharField(max_length=40)
    admin_group = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='group_admin')
    groupuser = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name


class GroupCorrespondence(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from_user')
    text = models.TextField(null=True, blank=True)
    textfile = models.FileField(upload_to='textfile_uploaded', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls'])])
    img = models.ImageField(upload_to='images_uploaded', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    send_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group.name

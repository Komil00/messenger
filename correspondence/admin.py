from django.contrib import admin
from .models import Correspondence, GroupCorrespondence, Group

admin.site.register(Correspondence)
admin.site.register(Group)
admin.site.register(GroupCorrespondence)


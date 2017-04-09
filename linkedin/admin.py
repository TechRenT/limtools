from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from . import models

# So we can be able to import and export data for LinkedinProfile class
class LinkedinResource(resources.ModelResource):

    class Meta:
        model = models.LinkedinProfile
        fields = ('id', 'profile_link')


@admin.register(models.LinkedinProfile)
class LinkedinProfileAdmin(ImportExportModelAdmin):
    resource_class = LinkedinResource

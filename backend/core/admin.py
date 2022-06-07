from django.contrib import admin

from core.models import ProjectEntry


class ProjectEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "owner")
    list_filter = ("rating", "owner")
    search_fields = ("name", "description")


admin.site.register(ProjectEntry, ProjectEntryAdmin)

from django.contrib import admin

from core.models import ProjectEntry, ProjectEntryWebHook


class ProjectEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "owner")
    list_filter = ("rating", "owner")
    search_fields = ("name", "description")


class ProjectEntryWebHookAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
    list_filter = ("owner",)
    search_fields = ("name",)


admin.site.register(ProjectEntry, ProjectEntryAdmin)
admin.site.register(ProjectEntryWebHook, ProjectEntryWebHookAdmin)

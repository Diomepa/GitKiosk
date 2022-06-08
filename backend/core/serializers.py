from rest_framework import serializers

from core.models import ProjectEntry, ProjectEntryWebHook


class ProjectEntrySerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProjectEntry
        fields = "__all__"


class ProjectEntryWebHookSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProjectEntryWebHook
        fields = "__all__"

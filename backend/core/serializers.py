from rest_framework import serializers

from core.models import ProjectEntry


class ProjectEntrySerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProjectEntry
        fields = "__all__"

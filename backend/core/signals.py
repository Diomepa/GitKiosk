from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import ProjectEntry
from core.serializers import ProjectEntrySerializer


@receiver(post_save, sender=ProjectEntry)
def post_save_handler(sender, **kwargs):
    item = kwargs.get("instance", None)
    created = kwargs.get("created", False)
    if created:
        data = ProjectEntrySerializer(item).data
        print(data)

import asyncio
import logging

import aiohttp
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import ProjectEntry, ProjectEntryWebHook
from core.serializers import ProjectEntrySerializer


async def call_hooks(data, hooks):
    # TODO: Does this even work properly? Check if it does (Attempt at concurrency)
    tasks = [hook_call(data, hook) for hook in hooks]
    await asyncio.gather(*tasks)


async def hook_call(data, hook: ProjectEntryWebHook):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(hook.link, data=data) as response:
                if response.status == 200:
                    result = await response.json()
                    logging.info(result.get("message"))
                else:
                    logging.warning(
                        f"{hook.link} returned with status {response.status}"
                    )
    except Exception as e:
        logging.error(e)


@receiver(post_save, sender=ProjectEntry)
def post_save_handler(sender, **kwargs):
    item = kwargs.get("instance", None)
    created = kwargs.get("created", False)
    if created:
        data = ProjectEntrySerializer(item).data
        # TODO: Figure out how to do this asynchronously,
        #  it will probably be much better off pushing to a queue anyhow
        hooks = list(ProjectEntryWebHook.objects.all())
        asyncio.run(call_hooks(data, hooks))

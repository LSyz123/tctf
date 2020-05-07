from handlers.models.system import SystemModel


async def get_title(self):
    try:
        system = await self.application.objects.get(SystemModel)
        return system.name
    except SystemModel.DoesNotExist:
        return self.settings['title']

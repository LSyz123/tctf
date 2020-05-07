from datetime import datetime

from handlers.models.system import SystemModel


async def started(self):
    result = {
        'status': False,
        'error': '比赛未开始'
    }

    system = await self.application.objects.get(SystemModel)
    if not system.game_mode:
        result['status'] = True
    else:
        now = datetime.now()
        if system.start < now < system.end:
            result['status'] = True
        elif now > system.end:
            result['error'] = '比赛已经结束'

    return result

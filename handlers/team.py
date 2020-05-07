from tornado import web
from tools.auth_wrap import authenticated_async
from handlers.models.user import UserModel
from tools.get_title import get_title


class TeamHandler(web.RequestHandler):
    @authenticated_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'index',
                     'logined': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'team': True}
        results = await self.application.objects.execute(UserModel.select())

        items = []
        for result in results:
            items.append(result)

        await self.render('team.html', base=base_info, items=items)

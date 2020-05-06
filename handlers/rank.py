from tornado import web

from handlers.models.user import UserModel
from tools.auth_wrap import authenticated_async


class RankHandler(web.RequestHandler):
    @authenticated_async
    async def get(self):
        base_info = {'title': 'CTF',
                     'module': 'index',
                     'logined': True,
                     'isadmin':self.current_user.admin,
                     'username': self.current_user.username,
                     'rank': True}
        results = await self.application.objects.execute(UserModel.select())
        items = []
        for res in results:
            if res.admin:
                continue
            items.append([res.username, res.rank])
        await self.render('rank.html', base=base_info, items=items)

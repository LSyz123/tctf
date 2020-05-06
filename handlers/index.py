from tornado import web
import jwt

from handlers.models.message import MessageModel
from handlers.models.user import UserModel


class IndexHandler(web.RequestHandler):
    async def get(self):
        base_info = {'title': 'CTF',
                     'module': 'index',
                     'logined': False}
        items = []
        token = self.get_cookie('token')
        if token:
            try:
                payload = jwt.decode(token, self.settings['secret_key'],
                                     algorithm=self.settings['secret_algorithm'],
                                     leeway=self.settings['jwt_expire'], options={'verify_exp': True})
                base_info['logined'] = True
                base_info['username'] = payload['username']
                user = await self.application.objects.get(UserModel, username=payload['username'])
                base_info['isadmin'] = user.admin
                results = await self.application.objects.execute(MessageModel.select())
                items = []
                for res in results:
                    items.append(res.message)

            except jwt.ExpiredSignatureError as e:
                pass
        await self.render('index.html', base=base_info, items=items)

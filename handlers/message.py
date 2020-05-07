from tornado.web import RequestHandler
import jwt

from handlers.models.user import UserModel
from tools.get_title import get_title


class MessageHandler(RequestHandler):
    async def get(self, message):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'message',
                     'logined': False, }
        token = self.get_cookie('token')
        if token:
            try:
                payload = jwt.decode(token, self.settings['secret_key'],
                                     algorithm=self.settings['secret_algorithm'],
                                     leeway=self.settings['jwt_expire'], options={'verify_exp': True})
                try:
                    user = await self.application.objects.get(UserModel, username=payload['username'])
                    base_info['logined'] = True
                    base_info['username'] = payload['username']
                    base_info['isadmin'] = user.admin
                except UserModel.DoesNotExist:
                    self.clear_cookie('token')
                    self.redirect('/')
            except jwt.ExpiredSignatureError:
                self.clear_cookie('token')
                self.redirect('/')
        await self.render('message.html', base=base_info, message=message)

from tornado.web import RequestHandler
import jwt

from handlers.models.user import UserModel


class MessageHandler(RequestHandler):
    async def get(self, message):
        base_info = {'title': 'CTF',
                     'module': 'message',
                     'logined': False, }
        token = self.get_cookie('token')
        if token:
            payload = jwt.decode(token, jwt.decode(token, self.settings['secret_key'],
                                                   algorithm=self.settings['secret_algorithm'],
                                                   leeway=self.settings['jwt_expire'],
                                                   options={'verify_exp': True}))
            if payload:
                base_info['logined'] = True
                base_info['username'] = payload['username']
                user = await self.application.objects.get(UserModel, username=payload['username'])
                base_info['isadmin'] = user.admin
        await self.render('message.html', base=base_info, message=message)

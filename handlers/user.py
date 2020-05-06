from tornado import web
from handlers.forms.user import RegisterForm, LoginForm
from handlers.models.message import MessageModel
from handlers.models.user import UserModel
from tools.auth_wrap import authenticated_async

import jwt
from datetime import datetime


class LoginHandler(web.RequestHandler):
    async def post(self):
        form_data = LoginForm(self.request.arguments)
        if form_data.validate():
            username = form_data.username.data
            password = form_data.password.data

            res = await self.application.objects.get(UserModel, username=username)

            if res:
                if res.password.check_password(password):
                    payload = {
                        'username': username,
                        'exp': datetime.utcnow()
                    }

                    token = jwt.encode(payload, self.settings['secret_key'],
                                       algorithm=self.settings['secret_algorithm'])
                    self.set_cookie('token', token.decode('utf-8'))

        self.redirect('/')


class RegisterHandler(web.RequestHandler):
    async def post(self):
        form_data = RegisterForm(self.request.arguments)
        if form_data.validate():
            username = form_data.username.data
            password = form_data.password.data
            email = form_data.email.data

            try:
                await self.application.objects.get(UserModel, username=username)
            except UserModel.DoesNotExist:
                await self.application.objects.create(UserModel, username=username, password=password, email=email)

        self.redirect('/')


class UserInfoHandler(web.RequestHandler):
    @authenticated_async
    async def get(self):
        base_info = {'title': 'CTF',
                     'module': 'UserInfo',
                     'logined': False}
        user = self.current_user
        await self.render('user.html', base=base_info, user=user)


class UserLogoutHandler(web.RequestHandler):
    @authenticated_async
    async def get(self):
        self.clear_cookie('token')
        self.redirect('/')

from tornado import web
from handlers.forms.user import RegisterForm, LoginForm
from handlers.models.user import UserModel
from tools.auth_wrap import authenticated_async

import jwt
from datetime import datetime

from tools.get_title import get_title


class LoginHandler(web.RequestHandler):
    async def post(self):
        form_data = LoginForm(self.request.arguments)
        if form_data.validate():
            username = form_data.username.data
            password = form_data.password.data
            try:
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
                    else:
                        self.redirect('/message/用户名或密码错误!')
                else:
                    self.redirect('/message/用户名或密码错误!')
            except UserModel.DoesNotExist:
                self.redirect('/message/用户名或密码错误!')
        else:
            self.redirect('/message/{}'.format(list(form_data.errors.values())[0][0]))

        if not self._finished:
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
        else:
            errors = form_data.errors.values()
            err_msg = ''
            for error in errors:
                err_msg += '{}    '.format(error[0])
            self.redirect('/message/{}'.format(list(form_data.errors.values())[0][0]))

        if not self._finished:
            self.redirect('/')


class UserInfoHandler(web.RequestHandler):
    @authenticated_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'UserInfo',
                     'logined': True,
                     'username': self.current_user.username,
                     'isadmin': self.current_user.admin}
        user = self.current_user
        await self.render('user.html', base=base_info, user=user)


class UserLogoutHandler(web.RequestHandler):
    @authenticated_async
    async def get(self):
        self.clear_cookie('token')
        self.redirect('/')

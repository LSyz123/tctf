from tornado import web
from handlers.forms.user import RegisterForm, LoginForm, UserInfoForm, PasswdForm
from handlers.models.buylog import BuylogModel
from handlers.models.chanllage import ChanllageModel
from handlers.models.hint import HintModel
from handlers.models.ranklog import RanklogModel
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
                     'userinfo': True,
                     'username': self.current_user.username,
                     'isadmin': self.current_user.admin}

        await self.render('user_info.html', base=base_info, current_user=self.current_user)

    @authenticated_async
    async def post(self):
        payload = UserInfoForm(self.request.arguments)
        if payload.validate():
            email = payload.email.data
            user = self.current_user
            user.email = email
            await self.application.objects.update(user)
        else:
            self.redirect('/message/{}'.format(list(payload.errors.values())[0][0]))
        if not self._finished:
            self.redirect('/user/')


class PasswdHandler(web.RequestHandler):
    @authenticated_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'UserInfo',
                     'logined': True,
                     'passwd': True,
                     'username': self.current_user.username,
                     'isadmin': self.current_user.admin}

        await self.render('user_passwd.html', base=base_info)

    @authenticated_async
    async def post(self):
        payload = PasswdForm(self.request.arguments)
        if payload.validate():
            user = self.current_user
            message = 'Success'
            if not user.password.check_password(payload.current_password.data):
                message = 'Wrong password!'
            user.password = payload.new_password.data
            await self.application.objects.update(user)
            self.redirect('/message/{}'.format(message))
        else:
            self.redirect('/message/{}'.format(list(payload.errors.values())[0][0]))


class UserlogHandler(web.RequestHandler):
    @authenticated_async
    async def get(self, log_type):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'UserInfo',
                     'logined': True,
                     'username': self.current_user.username,
                     'isadmin': self.current_user.admin}
        if log_type == 'buy':
            base_info['buylog'] = True
            query = BuylogModel.select(BuylogModel, HintModel) \
                .where(BuylogModel.user == self.current_user) \
                .join(HintModel).switch(BuylogModel)
            results = await self.application.objects.execute(query)
            logs = []
            for result in results:
                logs.append(result)
            await self.render('user_buylog.html', base=base_info, logs=logs)
        elif log_type == 'answer':
            base_info['answerlog'] = True
            query = RanklogModel.select(RanklogModel, ChanllageModel)\
                .where(RanklogModel.user==self.current_user)\
                .join(ChanllageModel).switch(RanklogModel)
            results = await self.application.objects.execute(query)
            logs = []
            for result in results:
                logs.append(result)
            await self.render('user_answerlog.html', base=base_info, logs=logs)
        else:
            self.redirect('/message/No such log type')


class UserLogoutHandler(web.RequestHandler):
    @authenticated_async
    async def get(self):
        self.clear_cookie('token')
        self.redirect('/')

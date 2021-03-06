import os
import time

import aiofiles
import random
from tornado.web import RequestHandler

from handlers.models.buylog import BuylogModel
from handlers.models.chanllage import ChanllageModel
from handlers.models.hint import HintModel
from handlers.models.ranklog import RanklogModel
from handlers.models.system import SystemModel
from handlers.models.type import TypeModel
from tools.auth_wrap import authenticated_isadmin_async
from handlers.models.user import UserModel
from handlers.models.message import MessageModel
from handlers.forms.admin import AddUserForm, AddChanllageForm, UpdateChanllageForm, AddNewsForm, SystemForm, \
    AddHintForm, AddTypeForm, UpdateUserForm
from tools.get_title import get_title


class AdminUser(RequestHandler):
    @authenticated_isadmin_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'Admin User',
                     'admin': True,
                     'user': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'logined': True}

        users = await self.application.objects.execute(UserModel.select())

        items = []
        for user in users:
            items.append([user.username, user.email, user.rank, user.admin])

        await self.render('admin_user.html', base=base_info, items=items)


class AdminUserAction(RequestHandler):
    @authenticated_isadmin_async
    async def get(self, action, username):
        if action == 'del':
            try:
                user = await self.application.objects.get(UserModel, username=username)
                await self.application.objects.delete(user)
            except UserModel.DoesNotExist:
                self.redirect('/message/找不到该用户!')
        elif action == 'setadmin':
            try:
                user = await self.application.objects.get(UserModel, username=username)
                user.admin = True
                await self.application.objects.update(user)
            except UserModel.DoesNotExist:
                self.redirect('/message/找不到该用户!')
        elif action == 'unsetadmin':
            try:
                user = await self.application.objects.get(UserModel, username=username)
                user.admin = False
                await self.application.objects.update(user)
            except UserModel.DoesNotExist:
                self.redirect('/message/找不到该用户!')
        elif action == 'view':
            try:
                user = await self.application.objects.get(UserModel, username=username)

                base_info = {'title': self.settings['title'],
                             'module': 'Admin User',
                             'admin': True,
                             'user': True,
                             'isadmin': self.current_user.admin,
                             'username': self.current_user.username,
                             'logined': True}

                await self.render('admin_user_view.html', base=base_info, user=user)
            except UserModel.DoesNotExist:
                self.redirect('/message/找不到该用户!')
        if not self._finished:
            self.redirect('/admin/user/')

    @authenticated_isadmin_async
    async def post(self, action, username=''):
        if action == 'add':
            payload = AddUserForm(self.request.arguments)
            if payload.validate():
                try:
                    await self.application.objects.get(UserModel, username=payload.username.data)
                except UserModel.DoesNotExist:
                    await self.application.objects.create(UserModel,
                                                          username=payload.username.data,
                                                          password=payload.password.data,
                                                          email=payload.email.data)
        elif action == 'update':
            payload = UpdateUserForm(self.request.arguments)
            if payload.validate():
                try:
                    user = await self.application.objects.get(UserModel, username=username)
                    user.username = payload.username.data
                    user.email = payload.email.data
                    user.rank = payload.rank.data
                    await self.application.objects.update(user)
                except UserModel.DoesNotExist:
                    self.redirect('/message/{}'.format(list(payload.errors.values())[0][0]))

        if not self._finished:
            self.redirect('/admin/user/')


class AdminChanllage(RequestHandler):
    @authenticated_isadmin_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'Admin Chanllage',
                     'admin': True,
                     'chanllage_admin': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'logined': True}

        items = []
        results = await self.application.objects.execute(ChanllageModel.select().dicts())
        for result in results:
            items.append([result['name'], result['describe'], result['rank']])

        types = []
        results = await self.application.objects.execute(TypeModel.select().dicts())
        for result in results:
            types.append(result['name'])

        await self.render('admin_chanllage.html', base=base_info, items=items, types=types)


class AdminChanllageAction(RequestHandler):
    @authenticated_isadmin_async
    async def get(self, action, name):
        if action == 'del':
            try:
                chanllage = await self.application.objects.get(ChanllageModel, name=name)
                await self.application.objects.delete(chanllage)
            except ChanllageModel.DoesNotExist:
                self.redirect('/message/找不到该赛题')
        elif action == 'view':
            try:
                chanllage = await self.application.objects.get(ChanllageModel, name=name)

                title = await get_title(self)
                base_info = {'title': title,
                             'module': 'Admin Chanllage',
                             'admin': True,
                             'chanllage_admin': True,
                             'isadmin': self.current_user.admin,
                             'username': self.current_user.username,
                             'logined': True}

                types = []
                results = await self.application.objects.execute(TypeModel.select().dicts())
                for result in results:
                    types.append(result['name'])

                current_type = await self.application.objects.get(TypeModel, id=chanllage.type_name_id)

                chanllage.file = chanllage.file.replace(self.settings['UPLOAD_BASE'], '')
                await self.render('admin_chanllage_view.html', base=base_info, chanllage=chanllage, types=types,
                                  current_type=current_type.name)
            except ChanllageModel.DoesNotExist:
                self.redirect('/message/找不到该赛题')
        if not self._finished:
            self.redirect('/admin/chanllage/')

    @authenticated_isadmin_async
    async def post(self, action, name=''):
        if action == 'add':
            payload = AddChanllageForm(self.request.arguments)
            if payload.validate():
                name = payload.name.data
                describe = payload.describe.data
                rank = payload.rank.data
                low = payload.low.data
                people = payload.people.data
                answer = payload.answer.data
                link = payload.link.data
                type_name = await self.application.objects.get(TypeModel, name=payload.type_name.data)
                upload_file = ''
                files_meta = self.request.files.get('upload_file', None)
                if files_meta:
                    while True:
                        upload_file = os.path.join(self.settings['UPLOAD_BASE'], ''.join(
                            random.sample('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST', 20)))
                        if not os.path.exists(upload_file):
                            break
                    async with aiofiles.open(upload_file, 'wb') as f:
                        await f.write(files_meta[0]['body'])

                try:
                    await self.application.objects.get(ChanllageModel, name=name)
                except ChanllageModel.DoesNotExist:
                    await self.application.objects.create(ChanllageModel, name=name,
                                                          describe=describe, rank=rank,
                                                          low=low, people=people, type_name=type_name,
                                                          answer=answer, file=upload_file,
                                                          link=link)
        elif action == 'update':
            payload = UpdateChanllageForm(self.request.arguments)
            if payload.validate():
                try:
                    chanllage = await self.application.objects.get(ChanllageModel, name=name)
                    chanllage.name = payload.name.data
                    chanllage.describe = payload.describe.data
                    chanllage.rank = payload.rank.data
                    chanllage.low = payload.low.data
                    chanllage.people = payload.people.data
                    chanllage.answer = payload.answer.data
                    chanllage.link = payload.link.data
                    await self.application.objects.update(chanllage)
                except ChanllageModel.DoesNotExist:
                    pass
        self.redirect('/admin/chanllage/')


class AdminHint(RequestHandler):
    @authenticated_isadmin_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'Admin Hint',
                     'admin': True,
                     'admin_hint': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'logined': True}

        chanllages = {}
        results = await self.application.objects.execute(ChanllageModel.select().dicts())
        for result in results:
            chanllages[result['id']] = result['name']

        items = []
        results = await self.application.objects.execute(HintModel.select().dicts())
        for result in results:
            items.append([chanllages[result['chanllage']], result['message'], result['sub_rank'], result['id']])

        await self.render('admin_hint.html', base=base_info, items=items, chanllages=chanllages.values())


class AdminHintAction(RequestHandler):
    @authenticated_isadmin_async
    async def get(self, action, id):
        if action == 'del':
            try:
                hint = await self.application.objects.get(HintModel, id=id)
                await self.application.objects.delete(hint)
            except HintModel.DoesNotExist:
                pass
        self.redirect('/admin/hint/')

    @authenticated_isadmin_async
    async def post(self, action, id=0):
        if action == 'add':
            payload = AddHintForm(self.request.arguments)
            if payload.validate():
                try:
                    chanllage = await self.application.objects.get(ChanllageModel, name=payload.chanllage.data)
                    await self.application.objects.create(HintModel,
                                                          chanllage=chanllage,
                                                          message=payload.message.data,
                                                          sub_rank=payload.sub_rank.data)
                except ChanllageModel.DoesNotExist:
                    self.redirect('/message/找不到该赛题！')
        if not self._finished:
            self.redirect('/admin/hint/')


class AdminNews(RequestHandler):
    @authenticated_isadmin_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'Admin Hint',
                     'admin': True,
                     'news': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'logined': True}

        items = []
        results = await self.application.objects.execute(MessageModel.select())
        for result in results:
            items.append([result.message, result.add_time])

        await self.render('admin_news.html', base=base_info, items=items)


class AdminNewsAction(RequestHandler):
    @authenticated_isadmin_async
    async def get(self, action, message):
        if action == 'del':
            news = await self.application.objects.get(MessageModel, message=message)
            await self.application.objects.delete(news)
        self.redirect('/admin/news/')

    @authenticated_isadmin_async
    async def post(self, action, message=''):
        if action == 'add':
            payload = AddNewsForm(self.request.arguments)
            if payload.validate():
                await self.application.objects.create(MessageModel, message=payload.message.data)
            else:
                self.redirect('/message/{}'.format(list(payload.errors.values())[0][0]))
        else:
            self.redirect('/message/无效的方法: {}'.format(action))

        self.redirect('/admin/news/')


class AdminSystem(RequestHandler):
    @authenticated_isadmin_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'Admin Hint',
                     'admin': True,
                     'system': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'logined': True}

        try:
            options = await self.application.objects.get(SystemModel)
        except SystemModel.DoesNotExist:
            await self.application.objects.create(SystemModel, name='CTF')
            options = await self.application.objects.get(SystemModel)

        await self.render('admin_system.html', base=base_info, options=options)

    @authenticated_isadmin_async
    async def post(self):
        payload = SystemForm(self.request.arguments)
        if payload.validate():
            name = payload.name.data
            game_mode = payload.game_mode.data
            start = payload.start.data
            end = payload.end.data
            try:
                system = await self.application.objects.get(SystemModel)
                system.name = name
                system.game_mode = game_mode
                system.start = start
                system.end = end
                await self.application.objects.update(system)
            except SystemModel.DoesNotExist:
                self.redirect('/message/Error')
        else:
            self.redirect('/message/{}'.format(list(payload.errors.values())[0][0]))
        if not self._finished:
            self.redirect('/admin/system/')


class AdminType(RequestHandler):
    @authenticated_isadmin_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'Admin Type',
                     'admin': True,
                     'type': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'logined': True}

        items = []
        results = await self.application.objects.execute(TypeModel.select().dicts())
        for result in results:
            items.append(result['name'])

        await self.render('admin_type.html', base=base_info, items=items)


class AdminTypeAction(RequestHandler):
    @authenticated_isadmin_async
    async def get(self, action, type_name):
        if action == 'del':
            try:
                _type = await self.application.objects.get(TypeModel, name=type_name)
                await self.application.objects.delete(_type)
            except TypeModel.DoesNotExist:
                self.redirect('/admin/type/')

        if not self._finished:
            self.redirect('/admin/type')

    @authenticated_isadmin_async
    async def post(self, action, type_name=''):
        if action == 'add':
            payload = AddTypeForm(self.request.arguments)
            if payload.validate():
                try:
                    await self.application.objects.get(TypeModel, name=payload.name.data)
                except TypeModel.DoesNotExist:
                    await self.application.objects.create(TypeModel, name=payload.name.data)

        self.redirect('/admin/type/')


class AdminLog(RequestHandler):
    @authenticated_isadmin_async
    async def get(self):
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'Admin Log',
                     'admin': True,
                     'logs': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'logined': True}

        logs = []
        query = RanklogModel.select()
        results = await self.application.objects.execute(query)
        for result in results:
            logs.append([result.user, result.chanllage,
                         result.event, result.answer,
                         result.uptime, result.rank])

        await self.render('admin_ranklog.html', base=base_info, logs=logs)


class AdminBuylog(RequestHandler):
    @authenticated_isadmin_async
    async def get(self):
        query = BuylogModel.select()
        logs = await self.application.objects.execute(query)
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'Admin Log',
                     'admin': True,
                     'buylogs': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'logined': True}

        await self.render('admin_buylog.html', base=base_info, logs=logs)

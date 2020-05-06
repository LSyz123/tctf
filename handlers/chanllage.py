from tornado.web import RequestHandler

from handlers.forms.chanllage import AnswerForm
from handlers.models.chanllage import ChanllageModel
from handlers.models.hintmodel import HintModel
from handlers.models.ranklog import RanklogModel
from handlers.models.type import TypeModel
from tools.auth_wrap import authenticated_async


class ChanllageHandler(RequestHandler):
    @authenticated_async
    async def get(self):
        base_info = {'title': 'CTF',
                     'module': 'index',
                     'logined': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'chanllage': True}

        types = []
        results = await self.application.objects.execute(TypeModel.select())
        for result in results:
            types.append(result)

        chanllages = []
        results = await self.application.objects.execute(ChanllageModel.select())
        for result in results:
            chanllages.append(result)

        items = {}
        keys = []
        for _type in types:
            keys.append(_type.name)
            items[_type.name] = []
            for chanllage in chanllages:
                if chanllage.type_name_id == _type.id:
                    items[_type.name].append(chanllage)

        for item in keys:
            if len(items[item]) == 0:
                items.pop(item)

        await self.render('chanllage.html', base=base_info, items=items)


class ChanllageViewHandler(RequestHandler):
    @authenticated_async
    async def get(self, name):
        base_info = {'title': 'CTF',
                     'module': 'index',
                     'logined': True,
                     'isadmin': self.current_user.admin,
                     'username': self.current_user.username,
                     'chanllage': True}

        try:
            chanllage = await self.application.objects.get(ChanllageModel, name=name)
            hints = []
            results = await self.application.objects.execute(HintModel.select().where(chanllage_id=chanllage.id))
            for result in results:
                hints.append(result.id)
            if chanllage.file != '':
                download_link = chanllage.file.replace(self.settings['UPLOAD_BASE'], '/static/uploads/')
            else:
                download_link = '#'
            await self.render('chanllage_view.html',
                              base=base_info, chanllage=chanllage,
                              download_link=download_link, hints=hints)
        except ChanllageModel.DoesNotExist:
            self.redirect('/message/找不到该赛题！')
        if not self._finished:
            self.redirect('/')


class AnswerHandler(RequestHandler):
    @authenticated_async
    async def post(self, name):
        try:
            chanllage = await self.application.objects.get(ChanllageModel, name=name)
            payload = AnswerForm(self.request.arguments)
            if payload.validate():
                try:
                    await self.application.objects.get(RanklogModel, user_id=self.current_user.id,
                                                       chanllage_id=chanllage.id,
                                                       event='Correct Answer of {}'.format(chanllage.name))
                except RanklogModel.DoesNotExist:
                    if payload.answer.data == chanllage.answer:
                        event = 'Correct Answer of {}'.format(chanllage.name)
                        rank = chanllage.rank
                        if chanllage.rank > chanllage.low and chanllage.people == 0:
                            rank = chanllage.low
                            chanllage.rank = chanllage.low
                        self.current_user.rank += rank
                        if chanllage.rank > chanllage.low and chanllage.people > 0:
                            chanllage.rank = chanllage.rank - (chanllage.rank - chanllage.low) / chanllage.people
                            chanllage.people -= 1
                        if chanllage.rank < chanllage.low:
                            chanllage.rank = chanllage.low
                        async with self.application.objects.atomic():
                            await self.application.objects.update(chanllage)
                            await self.application.objects.update(self.current_user)
                            await self.application.objects.create(RanklogModel, chanllage=chanllage,
                                                                  user=self.current_user, event=event,
                                                                  answer=payload.answer.data, rank=rank)
            else:
                self.redirect('/message/{}'.format(payload.error))
        except ChanllageModel.DoesNotExist:
            self.redirect('/message/找不到该赛题！')

        if not self._finished:
            self.redirect('/chanllage/')


class HintBuyHandler(RequestHandler):
    @authenticated_async
    async def get(self, chanllage_name, hint_id):
        try:
            hint = await self.application.objects.get(HintModel, hint_id=hint_id)
            event = 'Buy {} hint'.format(hint.id)
            try:
                await self.application.objects.get(RanklogModel,
                                                   uesr_id=self.current_user.id,
                                                   event=event)
            except RanklogModel.DoesNotExist:
                try:
                    chanllage = await self.application.objects.get(ChanllageModel,
                                                                   name=chanllage_name)
                    self.current_user.rank -= abs(hint.rank)
                    async with self.application.objects.atomic():
                        await self.application.objects.update(self.current_user)
                        await self.application.objects.create(RanklogModel, chanllage=chanllage,
                                                              user=self.current_user, event=event,
                                                              answer='', rank=hint.rank)
                except ChanllageModel.DoesNotExist:
                    self.redirect('/message/找不到该赛题！')
        except HintModel.DoesNotExist:
            self.redirect('/message/找不到该提示！')
        if not self._finished:
            self.redirect('/')

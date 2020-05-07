from tornado.web import RequestHandler

from handlers.forms.chanllage import AnswerForm
from handlers.models.chanllage import ChanllageModel
from handlers.models.ranklog import RanklogModel
from handlers.models.type import TypeModel
from tools.auth_wrap import authenticated_async
from tools.game_mode import started
from tools.get_title import get_title


class ChanllageHandler(RequestHandler):
    @authenticated_async
    async def get(self):
        game_status = await started(self)
        if not game_status['status']:
            self.redirect('/message/{}'.format(game_status['error']))
            await self.finish()
        title = await get_title(self)
        base_info = {'title': title,
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

        completed = []
        query = RanklogModel.select(RanklogModel, ChanllageModel)\
            .where(RanklogModel.user==self.current_user and RanklogModel.event=='Corrent')\
            .join(ChanllageModel).switch(RanklogModel)
        results = await self.application.objects.execute(query)
        for result in results:
            completed.append(result.chanllage)

        items = {}
        keys = []
        for _type in types:
            keys.append(_type.name)
            items[_type.name] = []
            for chanllage in chanllages:
                if chanllage.type_name_id == _type.id:
                    if chanllage.file != '':
                        download_link = chanllage.file.replace(self.settings['UPLOAD_BASE'], '/static/uploads/')
                    else:
                        download_link = '#'
                    chanllage.file = download_link
                    items[_type.name].append(chanllage)

        for item in keys:
            if len(items[item]) == 0:
                items.pop(item)

        await self.render('chanllage.html', base=base_info, items=items, completed=completed)


class AnswerHandler(RequestHandler):
    @authenticated_async
    async def post(self, name):
        game_status = await started(self)
        if not game_status['status']:
            self.redirect('/message/{}'.format(game_status['error']))
            await self.finish()
        try:
            chanllage = await self.application.objects.get(ChanllageModel, name=name)
            payload = AnswerForm(self.request.arguments)
            if payload.validate():
                try:
                    await self.application.objects.get(RanklogModel, user_id=self.current_user.id,
                                                       chanllage_id=chanllage.id,
                                                       event='Correct')
                except RanklogModel.DoesNotExist:
                    if payload.answer.data == chanllage.answer:
                        event = 'Correct'
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
                        event = 'Wrong'
                        await self.application.objects.create(RanklogModel, chanllage=chanllage,
                                                              user=self.current_user, event=event,
                                                              answer=payload.answer.data, rank=0)
                        self.redirect('/message/Wrong Answer!')
            else:
                self.redirect('/message/{}'.format(list(payload.errors.values())[0][0]))
        except ChanllageModel.DoesNotExist:
            self.redirect('/message/找不到该赛题!')

        if not self._finished:
            self.redirect('/chanllage/')


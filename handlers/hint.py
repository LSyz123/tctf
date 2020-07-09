from tornado.web import RequestHandler

from handlers.models.buylog import BuylogModel
from handlers.models.chanllage import ChanllageModel
from handlers.models.hint import HintModel
from handlers.models.user import UserModel
from tools.auth_wrap import authenticated_async
from tools.game_mode import started
from tools.get_title import get_title


class HintHandler(RequestHandler):
    @authenticated_async
    async def get(self):
        game_status = await started(self)
        if not game_status['status']:
            self.redirect('/message/{}'.format(game_status['error']))
            await self.finish()
        title = await get_title(self)
        base_info = {'title': title,
                     'module': 'hint',
                     'hint': True,
                     'username': self.current_user.username,
                     'isadmin': self.current_user.admin,
                     'logined': True}

        query = HintModel.select(HintModel, ChanllageModel). \
            join(ChanllageModel).switch(HintModel)
        results = await self.application.objects.execute(query)
        hints = []
        for result in results:
            hints.append(result)

        query = BuylogModel.filter(BuylogModel.user == self.current_user.username)
        results = await self.application.objects.execute(query)
        buyed = []
        for result in results:
            buyed.append(result.hint)
        await self.render('hint.html', base=base_info, hints=hints, buyed=buyed)


class HintBuyHandler(RequestHandler):
    @authenticated_async
    async def get(self, hint_id):
        try:
            hint = await self.application.objects.get(HintModel, id=hint_id)
            self.current_user.rank -= abs(hint.sub_rank)
            async with self.application.objects.atomic():
                await self.application.objects.update(self.current_user)
                await self.application.objects.create(BuylogModel, user=self.current_user.username,
                                                      hint=hint.message, rank=hint.sub_rank)
        except HintModel.DoesNotExist:
            self.redirect('/message/No such hint!')

        if not self._finished:
            self.redirect('/hint/')

from handlers.index import IndexHandler
from handlers.user import LoginHandler, SignupHandler, UserInfoHandler
from handlers.rank import RankHandler
from handlers.team import TeamHandler
from handlers.chanllage import ChanllageHandler
from tornado import web

urls = [
    web.URLSpec(r'/?', IndexHandler, name='Index'),
    web.URLSpec(r'/login/?', LoginHandler, name='Login'),
    web.URLSpec(r'/signup/?', SignupHandler, name='Signup'),
    web.URLSpec(r'/user/(\w+)/?', UserInfoHandler, name='UserInfo'),
    web.URLSpec(r'/rank/?', RankHandler, name='Rank'),
    web.URLSpec(r'/team/?', TeamHandler, name='Team'),
    web.URLSpec(r'/chanllage/?', ChanllageHandler, name='Chanllage'),
]
from handlers.hint import HintHandler, HintBuyHandler
from handlers.index import IndexHandler
from handlers.message import MessageHandler
from handlers.user import LoginHandler, RegisterHandler, UserInfoHandler, UserLogoutHandler, PasswdHandler, \
    UserlogHandler
from handlers.rank import RankHandler
from handlers.admin import AdminUser, AdminChanllage, AdminHint, AdminNews, AdminSystem, AdminUserAction, \
    AdminChanllageAction, AdminNewsAction, AdminHintAction, AdminType, AdminTypeAction, AdminLog, AdminBuylog
from handlers.chanllage import ChanllageHandler, AnswerHandler
from tornado import web

urls = [
    web.URLSpec(r'/?', IndexHandler, name='Index'),
    web.URLSpec(r'/login/?', LoginHandler, name='Login'),
    web.URLSpec(r'/register/?', RegisterHandler, name='Register'),
    web.URLSpec(r'/logout/?', UserLogoutHandler, name='Logout'),
    web.URLSpec(r'/user/?', UserInfoHandler, name='UserInfo'),
    web.URLSpec(r'/rank/?', RankHandler, name='Rank'),
    web.URLSpec(r'/chanllage/?', ChanllageHandler, name='Chanllage'),
    web.URLSpec(r'/answer/(.*)/?', AnswerHandler, name='UploadAnswer'),
    web.URLSpec(r'/admin/?', AdminUser, name='Admin'),
    web.URLSpec(r'/admin/user/?', AdminUser, name='AdminUser'),
    web.URLSpec(r'/admin/user/(\w+)/(.+)/?', AdminUserAction, name='AdminUserAction'),
    web.URLSpec(r'/admin/chanllage/?', AdminChanllage, name='AdminChanllage'),
    web.URLSpec(r'/admin/chanllage/(\w+)/(.+)/?', AdminChanllageAction, name='AdminChanllageAction'),
    web.URLSpec(r'/admin/hint/?', AdminHint, name='AdminHint'),
    web.URLSpec(r'/admin/hint/(\w+)/?', AdminHintAction, name='AdminHintAction_p'),
    web.URLSpec(r'/admin/hint/(\w+)/(.+)/?', AdminHintAction, name='AdminHintAction'),
    web.URLSpec(r'/admin/news/?', AdminNews, name='AdminNews'),
    web.URLSpec(r'/admin/news/(\w+)/(.+)/?', AdminNewsAction, name='AdminNewsAction'),
    web.URLSpec(r'/admin/system/?', AdminSystem, name='AdminSystem'),
    web.URLSpec(r'/admin/type/?', AdminType, name='AdminType'),
    web.URLSpec(r'/admin/type/(\w+)/(.+)/?', AdminTypeAction, name='AdminTypeAction'),
    web.URLSpec(r'/admin/logs/?', AdminLog, name='AdminLog'),
    web.URLSpec(r'/admin/buylogs/?', AdminBuylog, name='AdminBuylog'),
    web.URLSpec(r'/message/(.*)/?', MessageHandler, name='Message'),
    web.URLSpec(r'/hint/?', HintHandler, name='Hint'),
    web.URLSpec(r'/hint/buy/(\d+)/?', HintBuyHandler, name='BuyHint'),
    web.URLSpec(r'/user_passwd/?', PasswdHandler, name='ChangePassword'),
    web.URLSpec(r'/log/(\w+)/?', UserlogHandler, name='Userlog')
]

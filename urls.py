from handlers.index import IndexHandler
from handlers.message import MessageHandler
from handlers.user import LoginHandler, RegisterHandler, UserInfoHandler, UserLogoutHandler
from handlers.rank import RankHandler
from handlers.team import TeamHandler
from handlers.admin import AdminUser, AdminChanllage, AdminHint, AdminNews, AdminSystem, AdminUserAction, \
    AdminChanllageAction, AdminNewsAction, AdminHintAction, AdminType, AdminTypeAction, AdminLog
from handlers.chanllage import ChanllageHandler, ChanllageViewHandler, AnswerHandler
from tornado import web

urls = [
    web.URLSpec(r'/?', IndexHandler, name='Index'),
    web.URLSpec(r'/login/?', LoginHandler, name='Login'),
    web.URLSpec(r'/register/?', RegisterHandler, name='Register'),
    web.URLSpec(r'/logout/?', UserLogoutHandler, name='Logout'),
    web.URLSpec(r'/user/?', UserInfoHandler, name='UserInfo'),
    web.URLSpec(r'/rank/?', RankHandler, name='Rank'),
    web.URLSpec(r'/chanllage/?', ChanllageHandler, name='Chanllage'),
    web.URLSpec(r'/chanllage/view/(.*)/?', ChanllageViewHandler, name='ChanllageView'),
    web.URLSpec(r'/answer/(.*)/?', AnswerHandler, name='UploadAnswer'),
    web.URLSpec(r'/admin/?', AdminUser, name='Admin'),
    web.URLSpec(r'/admin/user/?', AdminUser, name='AdminUser'),
    web.URLSpec(r'/admin/user/(\w+)/?', AdminUserAction, name='AdminUserAction_p'),
    web.URLSpec(r'/admin/user/(\w+)/(.+)/?', AdminUserAction, name='AdminUserAction'),
    web.URLSpec(r'/admin/chanllage/?', AdminChanllage, name='AdminChanllage'),
    web.URLSpec(r'/admin/chanllage/(\w+)/?', AdminChanllageAction, name='AdminChanllageAction'),
    web.URLSpec(r'/admin/chanllage/(\w+)/(.+)/?', AdminChanllageAction, name='AdminChanllageAction'),
    web.URLSpec(r'/admin/hint/?', AdminHint, name='AdminHint'),
    web.URLSpec(r'/admin/hint/(\w+)/?', AdminHintAction, name='AdminHintAction_p'),
    web.URLSpec(r'/admin/hint/(\w+)/(.+)/?', AdminHintAction, name='AdminHintAction'),
    web.URLSpec(r'/admin/news/?', AdminNews, name='AdminNews'),
    web.URLSpec(r'/admin/news/(\w+)/?', AdminNewsAction, name='AdminNewsAction_p'),
    web.URLSpec(r'/admin/news/(\w+)/(.+)/?', AdminNewsAction, name='AdminNewsAction'),
    web.URLSpec(r'/admin/system/?', AdminSystem, name='AdminSystem'),
    web.URLSpec(r'/admin/type/?', AdminType, name='AdminType'),
    web.URLSpec(r'/admin/type/(\w+)/?', AdminTypeAction, name='AdminTypeAction'),
    web.URLSpec(r'/admin/type/(\w+)/(.+)/?', AdminTypeAction, name='AdminTypeAction_s'),
    web.URLSpec(r'/admin/logs/', AdminLog, name='AdminLog'),
    web.URLSpec(r'/message/(.*)/?', MessageHandler, name='message'),
]

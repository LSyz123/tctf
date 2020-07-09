import os

import peewee_async
from tornado import web, ioloop
from tornado.options import define, options
import tornado.httpserver
import urls
from handlers.models.system import SystemModel
from setting import settings, db

define('port', default=8000, help='Run on the given port', type=int)
define('debug', default=False, help='Debug mode', type=bool)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = web.Application(
        handlers=urls.urls,
        template_path=os.path.join(os.path.dirname(__file__), "template"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=options.debug,
        **settings
    )

    objects = peewee_async.Manager(db)
    db.set_allow_sync(False)
    app.objects = objects

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(4)

    tornado.ioloop.IOLoop.instance().start()

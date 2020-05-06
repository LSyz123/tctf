import os

import peewee_async
from tornado import web, ioloop
from tornado.options import define, options
import tornado.httpserver
import urls
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

    app.listen(options.port)

    objects = peewee_async.Manager(db)
    db.set_allow_sync(False)
    app.objects = objects

    tornado.ioloop.IOLoop.current().start()

import os
from tornado import web, ioloop
from tornado.options import define, options
import tornado.options
import tornado.httpserver
import urls

define('port', default=8000, help='Run on the given port', type=int)
define('debug', default=False, help='Debug mode', type=bool)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = web.Application(
        handlers=urls.urls,
        template_path=os.path.join(os.path.dirname(__file__), "template"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=options.debug
    )
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

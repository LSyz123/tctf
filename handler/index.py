from tornado import web


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('index.html', title='CTF', module='index', logined=False, items=['first', 'second'])

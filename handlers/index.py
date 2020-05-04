from tornado import web


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('index.html', title='CTF', module='123', logined=False, items=['first', 'second'])

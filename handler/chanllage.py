from tornado import web


class ChanllageHandler(web.RequestHandler):
    def get(self):
        return self.write('Chanllage')

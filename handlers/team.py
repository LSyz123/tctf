from tornado import web


class TeamHandler(web.RequestHandler):
    def get(self):
        return self.write('Team')

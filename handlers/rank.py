from tornado import web


class RankHandler(web.RequestHandler):
    def get(self):
        self.render('rank.html', title='CTF', module='Rank', rank=True, logined=False, items=[['admin', 100], ['test', 200]])

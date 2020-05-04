from tornado import web


class LoginHandler(web.RequestHandler):
    def post(self):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        self.render('index.html', team=True, title='CTF', module='index', logined=False, items=[username, password])


class SignupHandler(web.RequestHandler):
    def post(self):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        password_check = self.get_body_argument('password_check')
        email = self.get_body_argument('email')

        if password_check == password:
            message = '注册成功'
        else:
            message = '两次输入的密码不同'

        self.render('message.html', title='CTF', module='message', logined=False, message=message)


class UserInfoHandler(web.RequestHandler):
    def get(self, username):
        self.render('user.html', title='CTF', module='用户信息', logined=True, username=username)
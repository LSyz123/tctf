import functools
import jwt

from handlers.models.user import UserModel


def authenticated_async(method):
    @functools.wraps(method)
    async def wrapper(self, *args, **kwargs):
        token = self.get_cookie('token')
        if token:
            try:
                payload = jwt.decode(token, self.settings['secret_key'],
                                     leeway=self.settings['jwt_expire'], options={'verify_exp': True})
                username = payload["username"]

                try:
                    user = await self.application.objects.get(UserModel, username=username)
                    self._current_user = user

                    await method(self, *args, **kwargs)
                except UserModel.DoesNotExist as e:
                    self.clear_cookie('token')
                    self.redirect('/')
            except jwt.ExpiredSignatureError as e:
                self.clear_cookie('token')
                self.redirect('/')
            except jwt.InvalidSignatureError as e:
                self.clear_cookie('token')
                self.redirect('/')
        else:
            self.redirect('/')

    return wrapper


def authenticated_isadmin_async(method):
    @functools.wraps(method)
    async def wrapper(self, *args, **kwargs):
        token = self.get_cookie('token')
        if token:
            try:
                payload = jwt.decode(token, self.settings['secret_key'],
                                     leeway=self.settings['jwt_expire'], options={'verify_exp': True})
                username = payload["username"]

                try:
                    user = await self.application.objects.get(UserModel, username=username)
                    self._current_user = user
                    if user.admin:
                        await method(self, *args, **kwargs)
                    else:
                        self.redirect('/')
                except UserModel.DoesNotExist as e:
                    self.redirect('/')
            except jwt.ExpiredSignatureError as e:
                self.redirect('/')
        else:
            self.redirect('/')

    return wrapper
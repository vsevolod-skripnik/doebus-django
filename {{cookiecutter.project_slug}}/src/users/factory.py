from django.contrib.auth.models import AnonymousUser

from app.base.testing import register
from app.base.testing.types import FactoryProtocol
from users.models import User


@register
def user(self: FactoryProtocol, **kwargs: dict) -> User:
    return self.mixer.blend('users.User', **kwargs)


@register
def anon(self: FactoryProtocol, **kwargs: dict) -> AnonymousUser:
    return AnonymousUser()

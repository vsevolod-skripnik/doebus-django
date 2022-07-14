from functools import partial
from typing import Callable, Dict

from app.base.testing.mixer import mixer


def register(method: Callable) -> Callable:
    name = method.__name__
    FixtureRegistry.METHODS[name] = method
    return method


class FixtureRegistry:
    METHODS: Dict[str, Callable] = {}

    def get(self, name: str) -> Callable:
        method = self.METHODS.get(name)
        if not method:
            raise AttributeError(f'Factory method “{name}” not found.')
        return method


class FixtureFactory:
    def __init__(self) -> None:
        self.mixer = mixer
        self.registry = FixtureRegistry()

    def __getattr__(self, name: str) -> Callable:
        method = self.registry.get(name)
        return partial(method, self)

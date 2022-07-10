from abc import ABC
from abc import abstractmethod
from typing import Any


class BaseService(ABC):
    def __init__(self) -> None:
        ...

    def validate(self) -> None:
        ...

    def __call__(self) -> Any:
        self.validate()
        return self.act()

    @abstractmethod
    def act(self) -> Any:
        ...

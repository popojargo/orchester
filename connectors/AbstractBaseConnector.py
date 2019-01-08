from abc import ABC, abstractmethod
from typing import AnyStr


class AbstractBaseConnector(ABC):

    @abstractmethod
    def is_registered_to_group(self, username: AnyStr):
        pass

    @abstractmethod
    def remove_from_group(self, username: AnyStr):
        pass

    @abstractmethod
    def add_to_group(self, username: AnyStr):
        pass

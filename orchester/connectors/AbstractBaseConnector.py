from abc import ABC, abstractmethod
from typing import AnyStr

from orchester.Exceptions import RequestFailedError


class AbstractBaseConnector(ABC):

    @abstractmethod
    def is_registered_to_group(self, identifier: AnyStr):
        pass

    @abstractmethod
    def remove_from_group(self, identifier: AnyStr):
        pass

    @abstractmethod
    def add_to_group(self, identifier: AnyStr):
        pass


def normalize_exceptions(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as e:
            raise RequestFailedError(error_description=str(e))

    return func_wrapper

"""
Package which contains classes that implements object-like behaviour with dict
"""
from collections import OrderedDict


class BaseDTO(dict):
    """
    basic behaviour with "flat" dicts
    """
    def __setattr__(self, key, value):
        """
        setter
        :param key:
        :param value:
        :return:
        """
        self[key] = value

    def __getattr__(self, item):
        """
        getter
        :param item:
        :return:
        """
        try:
            return self[item]
        except KeyError:
            raise AttributeError


class DTO(BaseDTO):
    """
    for complex dicts
    """

    def __init__(self, data=None):
        """
        __init__ with hybrid behaviour
        :param data:
        """
        super().__init__()
        if data:
            if isinstance(data, (dict, OrderedDict)):
                for k, v in data.items():
                    setattr(self, k, self._construct(v))

    def _construct(self, data):
        """
        constructor for complex dicts
        :param data:
        :return:
        """
        if isinstance(data, (dict, OrderedDict)):
            for k, v in data.items():
                setattr(self, k, DTO()._construct(v))
            return self
        elif isinstance(data, list):
            _l = []
            for v in data:
                _l.append(DTO()._construct(v))
            return _l
        else:
            return data

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
    def __new__(cls, data=None):
        instance = super(DTO, cls).__new__(cls, data)
        if data:
            if isinstance(data, (dict, OrderedDict)):
                for k, v in data.items():
                    setattr(instance, k, DTO(v))
            elif isinstance(data, list):
                _l = []
                for v in data:
                    _l.append(DTO(v))
                instance = _l
            else:
                instance = data
        return instance

    def __init__(self, *args, **kwargs):
        """
        supressed
        :param args:
        :param kwargs:
        """
        pass

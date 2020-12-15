from collections import OrderedDict


class BasicDTO(dict):
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError


class DTO(BasicDTO):
    def __init__(self, data):
        super().__init__()
        self._construct(data)

    def _construct(self, data):
        if isinstance(data, (dict, OrderedDict)):
            for k, v in data.items():
                setattr(self, k, DTO(v))
            return self
        elif isinstance(data, list):
            _l = []
            for v in data:
                _l.append(DTO(v))
            return _l
        else:
            return data

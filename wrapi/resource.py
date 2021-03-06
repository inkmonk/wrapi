import core


class Resource(object):

    _resource_ = None

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __repr__(self):
        return str(self.id)

    @classmethod
    def get(cls, identifier, **kwargs):
        version = kwargs.pop("version")
        url = kwargs.pop("url")
        key = kwargs.pop("key")
        secret = kwargs.pop("secret")
        return cls(**core.get(cls._resource_, identifier, params=kwargs,
                   version=version, url=url, key=key,
                   secret=secret))

    @classmethod
    def all(cls, **kwargs):
        version = kwargs.pop("version")
        url = kwargs.pop("url")
        key = kwargs.pop("key")
        secret = kwargs.pop("secret")
        return [cls(**r_kwargs) for r_kwargs in core.all(
            cls._resource_, params=kwargs,
            version=version, url=url, key=key, secret=secret)]

    @classmethod
    def first(cls, **kwargs):
        kwargs['limit'] = 1
        resultset = cls.all(**kwargs)
        if len(resultset) == 0:
            return None
        return resultset[0]

    @classmethod
    def last(cls, **kwargs):
        kwargs['limit'] = 1
        kwargs['reverse'] = 'true'
        resultset = cls.all(**kwargs)
        if len(resultset) == 0:
            return None
        return resultset[0]

    @classmethod
    def create(cls, **kwargs):
        version = kwargs.pop("version")
        url = kwargs.pop("url")
        key = kwargs.pop("key")
        secret = kwargs.pop("secret")
        result = core.post(
            cls._resource_, data=kwargs, version=version, url=url,
            key=key, secret=secret)
        return cls(**result)

    @classmethod
    def create_all(cls, **kwargs):
        version = kwargs.pop("version")
        url = kwargs.pop("url")
        key = kwargs.pop("key")
        secret = kwargs.pop("secret")
        result = core.post(
            cls._resource_, data=kwargs, version=version, url=url,
            key=key, secret=secret)
        return [cls(**params) for params in result]

    @classmethod
    def update(cls, identifier, **kwargs):
        version = kwargs.pop("version")
        url = kwargs.pop("url")
        key = kwargs.pop("key")
        secret = kwargs.pop("secret")
        result = core.put(
            cls._resource_, identifier, data=kwargs, version=version,
            url=url, key=key, secret=secret)
        return cls(**result)

    @classmethod
    def patch(cls, identifier, **kwargs):
        version = kwargs.pop("version")
        url = kwargs.pop("url")
        key = kwargs.pop("key")
        secret = kwargs.pop("secret")
        result = core.put(
            cls._resource_, identifier, data=kwargs,
            version=version, url=url,
            key=key, secret=secret)
        return cls(**result)

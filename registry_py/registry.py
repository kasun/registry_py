import abc
from collections import defaultdict


class ClassNotRegistered(Exception):
    pass


class Registry(abc.ABC):
    _registry = defaultdict(dict)

    @classmethod
    def get_all_classes(cls):
        registry_name = cls.REGISTER_NAME
        return list(cls._registry[registry_name].values())

    @classmethod
    def register(cls, registering_cls, cls_id):
        registry_name = cls.REGISTER_NAME
        cls._registry[registry_name][cls_id] = registering_cls

    @classmethod
    def get_by_id(cls, cls_id):
        registry_name = cls.REGISTER_NAME
        try:
            return cls._registry[registry_name][cls_id]
        except KeyError:
            raise ClassNotRegistered(f"No registered class with ID: {cls_id}")


class Registrable:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        try:
            cls_id = getattr(cls, cls.REGISTRY_RECORD_ID)
        except AttributeError:
            pass
        else:
            cls.REGISTRY.register(cls, cls_id)


class ChannelRegistry(Registry):
    REGISTER_NAME = "Channel-Registry"


class BaseChannel(Registrable, abc.ABC):
    REGISTRY = ChannelRegistry
    REGISTRY_RECORD_ID = "CHANNEL_ID"


class EmailChannel(BaseChannel):
    CHANNEL_ID = 1

    def send(self):
        print("emailing")

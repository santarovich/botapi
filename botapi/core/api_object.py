from abc import ABCMeta
from typing import Optional

from .field import Field
from .mixins import FieldSerializeMixin


class BaseObjectMeta(ABCMeta):
    """
    Metaclass for creation api classes.

    Adds _fields and _aliases attributes.
    """

    def __new__(mcs, name, bases, attr):
        new_class = super().__new__(mcs, name, bases, attr)

        fields = set()
        aliases = {}

        for parent in bases:
            if isinstance(parent, BaseObjectMeta):
                fields.update(getattr(parent, '_fields'))
                aliases.update(getattr(parent, '_aliases'))

        for key, value in attr.items():
            if isinstance(value, Field):
                fields.add(key)
                if value.alias is not None:
                    aliases.update({key: value.alias})
                if value.self_base is True:
                    value.base = new_class

        setattr(new_class, '_aliases', aliases)
        setattr(new_class, '_fields', fields)
        return new_class


class BotObject(FieldSerializeMixin, metaclass=BaseObjectMeta):
    """
    Provide add data to serialize method.

    Inherit this class if you want to build your own api class
    """

    def serialize(self, data_to_update: Optional[dict] = None):
        """
        Serialize api object and add data_to_update to result

        :param data_to_update: updates result dict from passed dict
        :return: dict
        """
        result = super().serialize()
        if data_to_update is not None:
            result.update(data_to_update)
        return result

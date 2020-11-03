from botapi.core import Field, BaseObjectMeta, FieldSerializeMixin


class BaseViberObjectMeta(BaseObjectMeta):
    def __new__(mcs, name, bases, attr):
        attr.update({'_min_api_version': attr.pop('__min_api_version__', 1)})
        new_class = super().__new__(mcs, name, bases, attr)
        for parent in bases:
            if isinstance(parent, BaseViberObjectMeta):
                setattr(new_class, '_min_api_version', max(
                    getattr(new_class, '_min_api_version'),
                    getattr(parent, '_min_api_version')
                ))

        fields = getattr(new_class, '_fields', [])
        for field in fields:
            field_val = getattr(new_class, field)
            field_mav = getattr(field_val, 'min_api_version', 1)
            if getattr(field_val, 'default') is not None:
                setattr(new_class, '_min_api_version', max(
                    getattr(new_class, '_min_api_version'),
                    field_mav
                ))

        return new_class


class ViberObject(FieldSerializeMixin, metaclass=BaseViberObjectMeta):
    _min_api_version: int = 1

    def serialize(self, data_to_update: dict = None, add_min_api_ver: bool = None):
        result = super().serialize()
        if data_to_update is not None:
            result.update(data_to_update)
        if add_min_api_ver is True:
            result.update({'min_api_version': self._min_api_version})
        return result


class ViberField(Field):
    def __init__(
        self,
        base=None,
        self_base: bool = None,
        alias: str = None,
        default=None,
        min_api_version: int = None,
        validators=None
    ):
        super().__init__(
            base,
            self_base,
            alias,
            default,
            validators
        )
        if min_api_version is not None:
            self.min_api_version = min_api_version
        elif base is not None:
            if issubclass(base, ViberObject):
                self.min_api_version = getattr(base, '_min_api_version')
            else:
                self.min_api_version = 1
        else:
            self.min_api_version = 1

    def __set__(self, instance, value):
        super().__set__(instance, value)
        setattr(instance, '_min_api_version', max(
            getattr(instance, '_min_api_version'),
            self.min_api_version
        ))
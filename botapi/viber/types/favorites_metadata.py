from botapi.viber.types.base import ViberObject, ViberField


class FavoritesMetadata(ViberObject):
    """
    Represents a Viber favorites metadata object

    Examples:
    https://developers.viber.com/docs/tools/keyboards/#favorites-metadata
    """

    data_type = ViberField(alias='type')
    url = ViberField()
    title = ViberField()
    thumbnail = ViberField()
    domain = ViberField()
    width = ViberField()
    height = ViberField()
    alternative_url = ViberField(alias='alternativeUrl')
    alternative_text = ViberField(alias='alternativeText')

    def __init__(
        self,
        data_type: str,
        url: str,
        title: str = None,
        thumbnail: str = None,
        domain: str = None,
        width: int = None,
        height: int = None,
        alternative_url: str = None,
        alternative_text: str = None
    ):
        """
        Attr info: https://developers.viber.com/docs/tools/keyboards/#favorites-metadata
        """
        self.data_type = data_type
        self.url = url
        self.title = title
        self.thumbnail = thumbnail
        self.domain = domain
        self.width = width
        self.height = height
        self.alternative_url = alternative_url
        self.alternative_text = alternative_text

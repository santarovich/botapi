from botapi.viber.types.base import ViberField
from botapi.viber.types.message import Message


class UrlMessage(Message):
    """
    Represents a Viber url message object

    https://developers.viber.com/docs/api/rest-bot-api/#url-message
    """

    message_type = ViberField(default='url', alias='type')
    media = ViberField()

    def __init__(
        self,
        media: str,
        tracking_data: str = None
    ):
        """
        :param media: URL. Max 2,000 characters

        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            max 4000 characters
        """
        self.media = media
        self.tracking_data = tracking_data

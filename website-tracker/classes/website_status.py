import requests
from classes.terminal import TerminalColor


class WebsiteStatus:
    """Class responsible pairing each website with a status.

    Store information about the current status of the website.

    Attributes:
        website (str): Website address.
        mail_sent (bool): Monitors if a mail has been sent already.
        code (int): Latest HTTP status code.
    """

    def __init__(self, website: str) -> None:
        """WebsiteStatus object initialization.

        Args:
            website (str): Website address.
        """
        self.website = website
        self.mail_sent = False

        self.updateStatus()

    def updateStatus(self) -> None:
        """Update the status of the website."""
        try:
            self.code = requests.head(self.website).status_code
        except:
            self.code = 404

        match self.code:
            case 404:
                self.status = TerminalColor.DOWN.value

            case _:
                self.status = TerminalColor.OK.value

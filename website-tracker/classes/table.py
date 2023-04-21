from utils.misc import sanitizeURL
from tabulate import tabulate

from classes.website_status import WebsiteStatus
from classes.mail import Mail
from classes.terminal import TerminalMessage


class Table:
    """Class responsible for creating the table.

    Store information about the current status of the websites.

    Attributes:
        header (list[str]): Table headers.
        urls (list[str])): Website adresses.
        data (list[WebsiteStatus]): List of WebsiteStatus objects.
        table (list[list[str,str,int]]): Table matrix.
    """

    def __init__(self, urls: list[str]) -> None:
        """Mail object initialization.

        Sanitize the input urls and initialize the WebStatus objects.

        Args:
            urls (list[str]): List of URLs to retrieve.
        """
        self.header = ["Website URL", "Status", "HTTP Code"]
        self.urls = [sanitizeURL(url) for url in urls]
        self.data = [WebsiteStatus(url) for url in self.urls]
        self.table = [[item.website, item.status, item.code] for item in self.data]

    def updateData(self) -> None:
        """Get current status of the websites."""

        for item in self.data:
            item.updateStatus()

    def checkForMail(self, mail: Mail) -> None:
        """Check if a notification should be sent.

        Args:
            mail (Mail): Mail object with an active connection.
        """

        for item in self.data:
            if item.code == 404 and not item.mail_sent:
                mail.sendMail(item.website)
                item.mail_sent = True
            if item.code != 404 and item.mail_sent:
                item.mail_sent = False

    def display(self):
        """Display the table."""
        print(
            TerminalMessage.displayTable(
                tabulate(self.table, headers=self.header, tablefmt="outline")
            )
        )

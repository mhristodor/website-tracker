from utils.misc import sanitizeURL

from cli import terminal_message as tm

from classes.website_status import WebsiteStatus
from classes.mail import Mail


class Table:
    def __init__(self, urls: list[str]) -> None:
        self.header = ["Website URL", "Status", "HTTP Code"]
        self.urls = [sanitizeURL(url) for url in urls]
        self.data = [WebsiteStatus(url) for url in self.urls]
        self.table = [[item.website, item.status, item.code] for item in self.data]

    def display(self) -> None:
        tm.displayTable(self)

    def updateData(self) -> None:
        for item in self.data:
            item.updateStatus()

    def checkForMail(self, mail: Mail) -> None:
        for item in self.data:
            if item.code == 404 and not item.mail_sent:
                mail.sendMail(item.website)
                item.mail_sent = True

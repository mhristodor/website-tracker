from utils.misc import sanitizeURL

from cli import terminal_message as tm

from classes.website_status import WebsiteStatus


class Table:
    def __init__(self, urls: list[str]) -> None:
        self.header = ["Website URL", "Status", "HTTP Code"]
        self.urls = [sanitizeURL(url) for url in urls]
        self.data = [WebsiteStatus(url) for url in self.urls]
        self.table = [[item.website, item.status, item.code] for item in self.data]

    def display(self):
        tm.displayTable(self)

    def updateData(self):
        for item in self.data:
            item.updateStatus()

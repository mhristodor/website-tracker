import requests
from utils.enums import TerminalColor


class WebsiteStatus:
    def __init__(self, website: str) -> None:
        self.website = website

        self.updateStatus()

    def updateStatus(self) -> None:
        try:
            self.code = requests.head(self.website).status_code
        except:
            self.code = 404

        match self.code:
            case 200:
                self.status = TerminalColor.OK.value
            case 301:
                self.status = TerminalColor.REDR.value
            case _:
                self.status = TerminalColor.DOWN.value

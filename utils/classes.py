import requests


class WebsiteStatusCheck:
    def __init__(self, website: str) -> None:
        self.website = website

        self.status = requests.head(self.website).status_code

    def updateStatus(self) -> None:
        self.status = requests.head(self.website).status_code

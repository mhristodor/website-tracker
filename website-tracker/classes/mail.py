import smtplib
import os
import json

from email.mime.text import MIMEText
from datetime import datetime, timezone
from classes.terminal import TerminalMessage
from getpass import getpass


class Mail:
    """Mail class for handling connection and messages.

    Mail class implements server communication and mail delivery
    methods.

    Attributes:
        port (int): Default port for smtp connection set to 587.
        receiver (str): Recipient email address.
        creds (dict): Email credentials.
        server (smtplib.SMTP): Server object.
    """

    def __init__(self, receiver: str) -> None:
        """Mail object initialization.

        Args:
            receiver (str): Recipient email address.
        """

        self.port = 587
        self.receiver = receiver
        self.creds = self.loadCreds()

    def connectToServer(self) -> None:
        """Initialize server connection.

        Server attribute is created. Quits the
        application if the connection fails.

        """

        try:
            self.server = smtplib.SMTP(self.creds["smtp"], self.port)
        except:
            print(TerminalMessage.INVALID_SMTP.value)
            quit()
        return

    def loginToServer(self) -> None:
        """Initialize login connection.

        Quits the application if the connection fails.

        """

        try:
            self.server.ehlo()
            self.server.starttls()

            self.server.ehlo()
            self.server.login(self.creds["email"], self.creds["password"])
        except:
            print(TerminalMessage.INVALID_CREDS.value)
            quit()

        return

    def sendMail(self, url: str) -> None:
        """Implements mail notification utility.

        Creates a new mail notification and sends it to the
        receiver mail address.

        Args:
            url (str): URL included in the notification.

        """

        content = open("./template/mail.html", "r").read()

        content = content.replace("!url!", url.split("//")[-1])
        content = content.replace(
            "!time!", datetime.now(timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
        )

        msg = MIMEText(content, "html")

        msg["Subject"] = "Website Tracker Notification"
        msg["From"] = self.creds["email"]
        msg["To"] = self.receiver

        self.server.sendmail(self.creds["email"], [self.receiver], msg.as_string())

    def loadCreds(self) -> dict:
        """Implements configuration loading.

        Loads a file if it exists and returns the configuration
        or prompts the user to input the configuration from
        command line.

        Returns:
            config (dict): Mail configuration.

        """
        if not os.path.exists("./mail_config.json"):
            creds = {}

            print(TerminalMessage.NO_CREDS.value)

            print(TerminalMessage.INPUT_EMAIL.value, end="")
            creds["email"] = input()

            print(TerminalMessage.INPUT_SMTP.value, end="")
            creds["smtp"] = input()

            creds["password"] = getpass(TerminalMessage.INPUT_PASSWORD.value)

            with open("./mail_config.json", "w") as f:
                json.dump(creds, f, indent=4)

            return creds

        creds = json.load(open("./mail_config.json"))

        print(TerminalMessage.OK_CREDS.value)

        return creds

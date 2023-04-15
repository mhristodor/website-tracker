import smtplib, ssl
from cli import terminal_message as tm
from email.mime.text import MIMEText
from datetime import datetime, timezone


class Mail:
    def __init__(self, creds: dict, receiver: str) -> None:
        self.creds = creds
        self.port = 587
        self.receiver = receiver

    def connectToServer(self) -> None:
        try:
            self.server = smtplib.SMTP(self.creds["smtp"], self.port)
        except:
            tm.badSMTPSever()
            quit()
        return

    def loginToServer(self) -> None:
        try:
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.creds["email"], self.creds["password"])
        except:
            tm.badCredentials()
            quit()

        return

    def sendMail(self, url: str) -> None:
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

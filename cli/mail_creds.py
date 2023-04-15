import os
import json
from getpass import getpass
from cli import terminal_message as tm


def loadCreds() -> dict:
    if not os.path.exists("./mail_config.json"):
        creds = {}

        tm.noCredsFile()

        tm.enterEmail()
        creds["email"] = input()

        tm.enterSMTP()
        creds["smtp"] = input()

        creds["password"] = getpass("\033[93m[WARN]\033[0m Account Password: ")

        with open("./mail_config.json", "w") as f:
            json.dump(creds, f, indent=4)

        return creds

    creds = json.load(open("./mail_config.json"))

    tm.loadedCredentials()

    return creds

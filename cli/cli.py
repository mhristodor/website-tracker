from cli import parser
from cli.terminal_message import mainMessage
from cli.mail_creds import loadCreds

from classes.config import Config
from classes.file import FileHandler
from classes.table import Table
from classes.mail import Mail

from time import sleep
import signal

from utils.misc import move


def handler(signum, frame):
    exit(1)


def fileOperations(file: FileHandler) -> None:
    file.checkFileExists()
    file.checkFileUTF8()
    file.loadFile()
    file.loadURL()
    file.checkURL()


def mailOperations(mail: Mail) -> None:
    mail.connectToServer()
    mail.loginToServer()


def liveMode(table: Table, mail: Mail) -> None:
    SLEEP_TIME = 10
    TABLE_EXTRA_LINES = 8

    while True:
        table.display()
        sleep(SLEEP_TIME)
        table.updateData()
        table.checkForMail(mail)
        move(TABLE_EXTRA_LINES + len(table.urls))


def cli() -> None:
    signal.signal(signal.SIGINT, handler)

    args = parser.setupParser()

    mainMessage()

    config = Config(vars(args))
    config.display()

    file = FileHandler(config.path)

    fileOperations(file)

    if config.mail:
        mail = Mail(loadCreds(), config.mail)
        mailOperations(mail)

    table = Table(file.urls)

    if config.live:
        liveMode(table, mail)

    table.display()

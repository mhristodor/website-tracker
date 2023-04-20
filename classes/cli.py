from classes.file import FileHandler
from classes.mail import Mail
from classes.table import Table
from classes.terminal import TerminalMessage
from classes.config import Config

from utils.misc import move

from time import sleep


class CommandLineInterface:
    """Base class for application.

    Combines a Mail interface with Table object, a Config object
    and a FileHandler.

    Attributes:
        file (FileHandler): File containing URLs.
        table (Table): Table generated from URLs.
        mail (Mail): Mail interface.
        config (Config): Application configuration.
    """

    def __init__(self, config: dict) -> None:
        """Application initialization.

        Initializes several attributes with their respective classes.

        Args:
            config (dict): Arguments passed in the command line.
        """
        print(TerminalMessage.STARTUP.value)

        self.initializeConfig(config)

        self.file = FileHandler(self.config.path)
        self.table = Table(self.file.urls)

        self.mail = None

    def checkValidArgs(self, config: dict) -> None:
        """Verify if the arguments are valid.

        Args:
            config (dict): Arguments passed in the command line.

        """
        if config["mail"] and not config["live"]:
            print(TerminalMessage.INCOMPLETE_ARGS.value)
            exit()

    def initializeConfig(self, config: dict) -> None:
        """Initilizer for config attribute."""
        self.checkValidArgs(config)

        self.config = Config(**config)

        print(TerminalMessage.displayConfig(self.config.__dict__))

    def initializeMail(self) -> None:
        """Initilizer for mail attribute."""
        self.mail = Mail(self.config.mail)

        self.mail.connectToServer()
        self.mail.loginToServer()

    def display(self) -> None:
        """Display the table."""
        self.table.display()

    def liveUpdate(self) -> None:
        """Run until stopped from keyboard a live update of the table."""
        SLEEP_TIME = 10
        TABLE_EXTRA_LINES = 8

        while True:
            self.table.display()

            sleep(SLEEP_TIME)

            self.table.updateData()

            if self.mail:
                self.table.checkForMail(self.mail)

            move(TABLE_EXTRA_LINES + len(self.table.urls))

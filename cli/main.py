from cli import parser
from classes.cli import CommandLineInterface as cli
import signal


def handler(signum: any, frame: any) -> None:
    exit(1)


def main() -> None:
    signal.signal(signal.SIGINT, handler)

    cmdline = cli(parser.getArguments())

    if cmdline.config.mail:
        cmdline.initializeMail()

    if cmdline.config.live:
        cmdline.liveUpdate()

    cmdline.display()

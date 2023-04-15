import argparse


def setupParser() -> argparse.ArgumentParser.parse_args:
    parser = argparse.ArgumentParser(
        description="Track website availability from command line."
    )

    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Path to an input file containing the website URLs.",
        required=True,
    )

    parser.add_argument(
        "-l",
        "--live",
        help="Keep runing until CTRL-C is pressed. Checks are performed every 10 seconds.",
        required=False,
        action="store_true",
    )

    parser.add_argument(
        "-m",
        "--mail",
        type=str,
        help="Mail adress to send an alert when an website is down",
        required=False,
    )

    return parser.parse_args()

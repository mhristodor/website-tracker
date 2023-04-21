import argparse


def getArguments() -> dict:
    """Obtain arguments using argparse utility.

    Defines argparse functionality and returns a
    dictionary with arguments.

    Returns:
        dict: Dictionary of arguments passed at runtime.

    """
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

    return vars(parser.parse_args())

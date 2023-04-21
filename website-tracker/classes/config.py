from dataclasses import dataclass


@dataclass
class Config:
    """Configuration class for the command line application.

    It contains the configuration passed at the command
    line.


    Attributes:
        path (str): Path to a file containing a list of websites.
        live (bool): Switch between live mode and one time mode.
        mail (str): Mail adress where notifications will be sent.

    """

    path: str
    live: bool = False
    mail: str = None

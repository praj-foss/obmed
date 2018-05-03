"""

obmed - Openbox menu editor

Usage:
    obmed read [--menu <FILE>]
    obmed add <line_number> [--menu <FILE>]
    obmed remove <line_number> [--menu <FILE>]
    obmed modify <line_number> [--menu <FILE>]
    obmed -v | --version

Options:
    -h, --help                      Prints this help message.
    -v, --version                   Prints the version.
    -m <FILE>, --menu <FILE>        Specify the menu.xml file. [default: ~/.config/openbox/menu.xml]
"""

from docopt import docopt
from os.path import expanduser
import actions


def main():
    args = docopt(__doc__)

    if args["--version"]:
        import obmed
        print(obmed.__version__)

    if args["read"]:
        actions.read_menu(expanduser(args["--menu"]))


if __name__ == "__main__":
    main()

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
    -m <FILE>, --menu <FILE>        Specify the menu.xml file.
                                    [default: ~/.config/openbox/menu.xml]
"""

__version__ = "0.0.1"

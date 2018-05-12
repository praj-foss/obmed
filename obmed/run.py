from docopt import docopt
from os.path import expanduser
from obmed import __doc__
from obmed.actions import read_menu, add_entry


def main():
    args = docopt(__doc__)

    # print(args)

    if args["--version"]:
        import obmed
        print(obmed.__version__)

    if args["read"]:
        read_menu(expanduser(args["--menu"]))

    if args["add"]:
        add_entry(args["<line_number>"])


if __name__ == "__main__":
    main()

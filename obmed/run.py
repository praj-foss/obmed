from docopt import docopt
from os.path import expanduser
from obmed import __doc__, __version__, menuparser


def main():
    args = docopt(__doc__)

    # print(args)
    menuparser.load(expanduser(args["--menu"]))

    if args["--version"]:
        print(__version__)

    if args["print"]:
        menuparser.activate_print()

    if args["add"]:
        menuparser.activate_add(args["<line_number>"])


if __name__ == "__main__":
    main()

import os.path
from xml.etree.ElementTree import parse
from obmed.commands import printmenu


is_active = {"print": False,
             "add": False,
             "remove": False,
             "modify": False}
target_line_number = None
line_number = 0


class MenuParsingException(Exception):
    pass


def load(file):
    if not os.path.isfile(file):
        print("Cannot access the file:", file)
        exit()
    else:
        print("Given menu file:", file)
        global root_menu
        root_menu = parse(file).getroot()[0]


def is_valid_element(element):
    # that [21:] is a quick hack for removing "{http://openbox.org/}" from front
    return element.tag[21:] in ["separator", "item", "menu"]


def activate_print():
    is_active["print"] = True

    print("\n\tOPENBOX MENU")
    cycle_tree(root_menu)

    is_active["print"] = False


def activate_add(target):
    global target_line_number
    target_line_number = target
    is_active["add"] = True

    try:
        cycle_tree(root_menu)
    except MenuParsingException:
        print("New entry added to line number", target)

    is_active["add"] = False


def cycle_tree(element):
    for child in element:
        if not is_valid_element(child):
            continue

        global line_number
        line_number += 1

        if is_active["print"]:
            printmenu.print_all(line_number, child, element)

        if is_active["add"] and line_number == target_line_number:
            raise MenuParsingException

        if is_active["remove"] and line_number == target_line_number:
            raise MenuParsingException

        if is_active["modify"] and line_number == target_line_number:
            raise MenuParsingException

        cycle_tree(child)

        printmenu.pop_stack()

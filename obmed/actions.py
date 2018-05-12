import os.path
from xml.etree.ElementTree import parse
import read


execute_read = False
execute_add = False
execute_remove = False
execute_modify = False
target_line_number = None

line_number = 0


def validate(file):
    if not os.path.isfile(file):
        print("Cannot access the file:", file)
        exit()
    else:
        print("Given menu file:", file)


def is_valid_element(element):
    # that [21:] is a quick hack for removing "{http://openbox.org/}" from front
    return element.tag[21:] in ["separator", "item", "menu"]


def read_menu(file):
    validate(file)
    root_menu = parse(file).getroot()[0]

    global execute_read
    execute_read = True

    print("\n\tOPENBOX MENU")
    cycle_tree(root_menu)

    execute_read = False


def add_entry(target):
    print("New entry added to line number", target)


def cycle_tree(element):
    for child in element:
        if not is_valid_element(child):
            continue
            
        if execute_read:
            read.print_all(line_number, child, element)

        cycle_tree(child)

        read.pop_stack()

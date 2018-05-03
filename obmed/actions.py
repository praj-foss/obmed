import os.path
import xml.etree.ElementTree as et


line_number = 0
box_line_stack = []
LINE_0 = "    "
LINE_1 = "│   "
LINE_2 = "├── "
LINE_3 = "└── "


def validate(file):
    if not os.path.isfile(file):
        print("Cannot access the file:", file)
        exit()
    else:
        print("Given menu file:", file)


def read_menu(file):
    validate(file)
    root_menu = et.parse(file).getroot()[0]

    print("\n\tOPENBOX MENU")
    cycle_tree(root_menu)


def is_separator(element):
    return "separator" in element.tag


def is_valid_element(element):
    # that [21:] is a quick hack for removing "{http://openbox.org/}" from front
    return element.tag[21:] in ["separator", "item", "menu"]


def is_last_in_menu(child, parent):
    return child == parent[-1]


def print_line_number():
    global line_number
    line_number += 1
    print(line_number, end="\t")


def print_box_line_stack():
    for line in box_line_stack:
        print(line, end="")


def print_box_line_attached(child, parent):
    if is_last_in_menu(child, parent):
        print(LINE_3, end="")
    else:
        print(LINE_2, end="")


def print_element_name(element):
    if is_separator(element):
        print("[SEPARATOR]", end=" ")
    if "label" in element.attrib:
        print(element.attrib["label"])
    else:
        print()


def cycle_tree(element):
    for child in element:
        if not is_valid_element(child):
            continue

        print_line_number()
        print_box_line_stack()
        print_box_line_attached(child, element)
        print_element_name(child)

        if is_last_in_menu(child, element):
            box_line_stack.append(LINE_0)
        else:
            box_line_stack.append(LINE_1)

        cycle_tree(child)
        box_line_stack.pop()

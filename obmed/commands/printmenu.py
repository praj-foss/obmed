box_line_stack = []
LINE_0 = "    "
LINE_1 = "│   "
LINE_2 = "├── "
LINE_3 = "└── "


def is_separator(element):
    return "separator" in element.tag


def is_last_in_menu(child, parent):
    return child == parent[-1]


def print_line_number(line_number):
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


def print_all(line_number, child, element):
    print_line_number(line_number)
    print_box_line_stack()
    print_box_line_attached(child, element)
    print_element_name(child)

    if is_last_in_menu(child, element):
        box_line_stack.append(LINE_0)
    else:
        box_line_stack.append(LINE_1)


def pop_stack():
    box_line_stack.pop()

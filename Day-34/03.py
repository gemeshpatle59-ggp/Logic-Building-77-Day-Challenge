# Print all elements of a list recursively.

def print_element(lists):
    if lists == []:
        return

    print(lists[0])

    return print_element(lists[1:])

(print_element([1,2,3]))
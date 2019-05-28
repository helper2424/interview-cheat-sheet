from node import Node

def reverse_to(list, to, include):
    cursor = list
    new_list = None
    condition = True
    while condition:
        if cursor is to:
            condition = False
            if not include:
                break
            else:
                cursor = Node(cursor.value)

        next_i = cursor.next
        cursor.next = new_list
        new_list = cursor
        cursor = next_i

    return new_list

def is_palindrom(list):
    if list is None:
        return True

    middle = list
    end = list
    even = False
    while not end is None:
        if middle.next is None:
            break

        end = end.next

        if end is None:
            even = True
            break
        else:
            end = end.next
            even = False

        middle = middle.next

    revere_first_part = reverse_to(list, middle, even)
    while revere_first_part and middle:
        if not revere_first_part.value == middle.value:
            return False
        revere_first_part = revere_first_part.next
        middle = middle.next

    return True
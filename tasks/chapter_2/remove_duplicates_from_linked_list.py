from node import Node

def remove_duplicates(linked_list):
    cache = dict()

    cursor = linked_list
    prev = None
    while(cursor != None):
        next_item = cursor.next
        if cache.get(cursor.value):
            if prev:
                prev.next = next_item
            cursor.next = None
        else:
            cache[cursor.value] = True
            prev = cursor
        cursor = next_item

    return linked_list

def remove_duplicates_without_buffer(linked_list):
    cursor = linked_list
    while(cursor != None):
        internal_cursor = cursor.next
        prev = cursor
        while (internal_cursor != None):
            next_item = internal_cursor.next
            if internal_cursor.value == cursor.value:
                if prev:
                    prev.next = next_item
                internal_cursor.next = None
            else:
                prev = internal_cursor
            internal_cursor = next_item

        cursor = cursor.next

    return linked_list
def add_node_to_end(item, first, last):
    if not first:
        first = item
        last = item
    last.next = item
    last = item
    last.next = None

    return (first, last)

def sort(linked_list, x):
    if linked_list == None:
        return linked_list

    before = None
    after = None
    before_end = None
    after_end = None

    cursor = linked_list

    while cursor != None:
        item = cursor
        cursor = cursor.next
        if item.value >= x:
            after, after_end = add_node_to_end(item, after, after_end)
        else:
            before, before_end = add_node_to_end(item, before, before_end)

    if before == None:
        return after
    elif after == None:
        return before

    before_end.next = after

    return before

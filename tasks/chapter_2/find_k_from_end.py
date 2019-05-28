def find_k_from_end(linked_list, k):
    current_cursor = linked_list
    plus_k_cursor = linked_list

    if linked_list == None:
        return linked_list

    for i in range(k):
        plus_k_cursor = plus_k_cursor.next
        if not plus_k_cursor:
            return None

    while plus_k_cursor.next != None:
        plus_k_cursor = plus_k_cursor.next
        current_cursor = current_cursor.next

    return current_cursor

def recursion(linked_list, k):
    if linked_list == None:
        return (None, -1)

    result = recursion(linked_list.next, k)

    if result[1] == k:
        return result

    return (linked_list, result[1] + 1)

def find_k_from_end_recursive(linked_list, k):
    result = recursion(linked_list, k)

    if k > result[1]:
        return None

    return result[0]
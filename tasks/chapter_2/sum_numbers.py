from node import Node

def sum(a, b):
    result = None
    result_end = None
    value = 0
    while a or b or value > 0:
        if a:
            value += a.value
            a = a.next

        if b:
            value += b.value
            b = b.next

        new_item = Node(value % 10)
        if not result:
            result = new_item
            result_end = result
        else:
            result_end.next = new_item
            result_end = new_item

        if value < 10:
            value = 0
        else:
            value = 1

    return result

def recursion_sum(a, b, start = False):
    if not a and not b:
        return (0, None)

    node = Node(0)
    prev_sum = recursion_sum(a.next, b.next)

    value = a.value + b.value + prev_sum[0]
    node.value = value % 10
    node.next = prev_sum[1]

    if start and value // 10 > 0:
        root = Node(value // 10)
        root.next = node
        node = root

    return (value // 10, node)

def sum_forward_order(a, b):
    if not a and not b:
        return None

    length_a = 0
    length_b = 0
    a_c = a
    b_c = b

    while a_c or b_c:
        if a_c:
            length_a += 1
            a_c = a_c.next

        if b_c:
            length_b += 1
            b_c = b_c.next

    a_c = a
    b_c = b

    shortest = a_c if length_a < length_b else b_c

    for i in range(abs(length_b - length_a)):
        newItem = Node(0)
        newItem.next = shortest
        shortest = newItem

    if length_a < length_b:
        a_c = shortest
    else:
        b_c = shortest

    return recursion_sum(a_c, b_c, True)[1]
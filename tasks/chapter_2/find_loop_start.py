from node import Node

def find_loop_start(linked_list):
    fast = linked_list
    slow = linked_list

    while not slow is None:
        slow = slow.next

        if slow is None:
            return linked_list

        slow = slow.next

        fast = fast.next

        if slow is fast:
            break

    fast = linked_list
    while slow is not fast:
        fast = fast.next
        slow = slow.next

    return slow
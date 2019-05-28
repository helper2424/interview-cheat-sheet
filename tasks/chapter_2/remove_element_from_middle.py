def remove_from_middle(node):
    next_item = node.next
    node.value = next_item.value
    node.next = next_item.next
    next_item.next = None

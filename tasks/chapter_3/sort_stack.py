def sort(stack):
    buffer = []

    if len(stack) == 0:
        return

    while len(stack) > 0:
        buffer.append(stack.pop())

    while len(buffer) > 0:
        item = buffer.pop()

        moved_items = 0

        while len(stack) and stack[-1] < item:
            buffer.append(stack.pop())
            moved_items += 1

        stack.append(item)

        while moved_items > 0:
            stack.append(buffer.pop())
            moved_items -= 1


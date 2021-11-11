def moveDisks(n, fromTower, toTower, buffer):
    if n <= 0:
        return

    moveDisks(n - 1, fromTower, buffer, toTower)

    toTower.append(fromTower.pop())

    moveDisks(n - 1, buffer, toTower, fromTower)

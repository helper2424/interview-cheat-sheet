class StackWithMin:
    def __init__(self):
        self.internal = []
        self.mins = []

    def push(self, value):
        if len(self.mins) == 0 or value <= self.mins[-1]:
            self.mins.append(value)

        self.internal.append(value)

    def pop(self):
        value = self.internal.pop()
        if self.min() == value:
            self.mins.pop()

        return value

    def min(self):
        return self.mins[-1]

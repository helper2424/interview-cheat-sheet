class Queue2Stacks:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []


    def push(self, value):
       self.push_stack.append(value)


    def pop(self):
        if len(self.pop_stack) == 0:
            self._move_to_pop_stack()

        if len(self.pop_stack) == 0:
            return None

        return self.pop_stack.pop()


    def peek(self):
        if len(self.pop_stack) == 0:
            self._move_to_pop_stack()

        if len(self.pop_stack) == 0:
            return None

        return self.pop_stack[-1]


    def to_array(self):
        return self.push_stack[::-1] + self.pop_stack


    def _move_to_pop_stack(self):
        while len(self.push_stack) > 0:
            self.pop_stack.append(self.push_stack.pop())

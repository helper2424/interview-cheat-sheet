class Stack:
    DEFAULT_SIZE = 3
    STACKS_COUNT = 3

    def __init__(self):
        self.internal = [None] * Stack.DEFAULT_SIZE * Stack.STACKS_COUNT
        self.stack_pointers = [i * Stack.DEFAULT_SIZE for i in range(Stack.STACKS_COUNT)]
        self.stack_starts = self.stack_pointers.copy()

    def push(self, stack_number, value):
        if stack_number >= Stack.STACKS_COUNT or stack_number < 0:
            raise ValueError('Incorrect stackNumber')

        sp = self.__get_stack_pointer__(stack_number)
        sb = self.__stack_border__(stack_number)

        if sp < sb:
            self.internal[sp] = value
            self.__set_stack_pointer__(stack_number, sp + 1)
        elif stack_number == Stack.STACKS_COUNT:
            self.internal.append(value)
            self.__set_stack_pointer__(stack_number, sp + 1)
        else:
            self.internal = self.__extend_and_copy__(self.internal, stack_number)
            self.push(self, stack_number, value)

    def pop(self, stackNumber):
        pass

    def peek(self, stackNumber):
        pass

    def __get_stack_pointer__(self, stack_number):
        return self.stack_pointers[stack_number]

    def __set_stack_pointer__(self, stack_number, pointer):
        self.stack_pointers[stack_number] = pointer

    def __stack_border__(self, stack_number):
        return (stack_number + 1) * Stack.DEFAULT_SIZE

    def __stack_item_size__(self, stack_number):

    def __extend_and_copy__(self, array, number):
        new_size = len(array) + self.__stack_item_size__(number)
        result = [None]*new_size

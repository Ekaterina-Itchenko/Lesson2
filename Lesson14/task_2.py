class ValidationError(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        return self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]


def is_correct_bracket(brackets) -> bool:
    """The function takes the string consisting of brackets
     and returns 'True', if all brackets are closed, or 'False'
     otherwise"""
    if not brackets:
        return False
    stack = Stack()
    for char in brackets:
        if char in '({[':
            stack.push(char)
        elif char == ")" and stack.pop() != "(":
            return False
        elif char == "]" and stack.pop() != "[":
            return False
        elif char == "}" and stack.pop() != "{":
            return False
        elif char not in '()[]{}':
            raise ValueError('All symbols must be brackets')

    return stack.is_empty()


print(is_correct_bracket('({})'))

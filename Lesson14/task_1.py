class Alphabet:
    def __init__(self, end, lower=True):
        self.end = end
        self.lower = lower

    def __iter__(self):
        self.index_lower = ord('a')
        self.index_upper = ord('A')
        return self

    def __next__(self):
        if (self.index_lower == ord(self.end.lower()) + 1 and
                self.lower is True):
            raise StopIteration
        elif (self.index_upper == ord(self.end.upper()) + 1 and
              self.lower is False):
            raise StopIteration
        elif self.index_lower <= ord(self.end.lower()) and self.lower is True:
            result = chr(self.index_lower)
            self.index_lower += 1
            return result
        else:
            result = chr(self.index_upper)
            self.index_upper += 1
            return result


a1 = Alphabet('j')

for i in a1:
    print(i)

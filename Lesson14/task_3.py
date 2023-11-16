from functools import total_ordering


class IncorrectDataError(Exception):
    ...


@total_ordering
class Element:
    def __init__(self, data):
        self._data = data
        self.next = None

    @property
    def data(self):
        if self._data in range(0, 10000):
            return self._data
        else:
            raise IncorrectDataError('The element must be'
                                     ' from 0 to 10000')

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, element):
        current_element = Element(element)
        if not self.head:
            self.head = current_element
        else:
            last_element = self.head
            while last_element.next:
                last_element = last_element.next
            last_element.next = current_element

    def reverse(self):
        previous_element = None
        current_element = self.head
        while current_element:
            next_element = current_element.next
            current_element.next = previous_element
            previous_element = current_element
            current_element = next_element
        self.head = previous_element

    def println(self):
        result = []
        if not self.head:
            return result
        current_element = self.head
        while current_element:
            result.append(current_element.data)
            current_element = current_element.next
        return result

    def length(self):
        current_element = self.head
        count = 1
        if not self.head:
            return 0
        while current_element.next:
            count += 1
            current_element = current_element.next
        return count

    def __iter__(self):
        current_element = self.head
        while current_element is not None:
            yield current_element
            current_element = current_element.next


# my_list = LinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# print(my_list.println())
#
# my_list.reverse()
# print(my_list.println())
#
# print(my_list.length())
#
# for i in my_list:
#     print(i.data)

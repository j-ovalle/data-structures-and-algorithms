from linked_list import LinkedList

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        # Push or add new element onto the top of the stack
        self.ll.insert_first(new_element)

    def pop(self):
        # Pop or remove the first element off the top of the stack and return it
        return self.ll.delete_first()

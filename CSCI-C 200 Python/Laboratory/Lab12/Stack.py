class Stack:

    def __init__(self):
        """
        Initializes the stack as a data structure such as a list or 
        an array
        """
        self.data = []
    

    def pop(self):
        """
        Removes the first item from the stack.
        Implemented so that there is not an error if the start
        is empty
        """
        if not self.isEmpty():
            return self.data.pop()
        else:
            return None

    def push(self, item):
        """
        Pushes an item on to a stack
        """
        self.data.append(item)
    

    def isEmpty(self):
        """
        Returns True is stack is empty, False otherwise
        """
        if self.data:
            return False
        return True
    
    def peek(self):
        """
        Shows what the first item on the stack is. Will keep the stack
        the same, since you just want to see what the value is.
        Returns the item on the top of te stack
        """
        if not self.isEmpty():
            return self.data[0]
        else:
            return None

    
    def __str__(self):
        return str(self.data)
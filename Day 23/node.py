class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def display(self):
        if self.next:
            print(self.value, self.next.value)
        else:
            print(self.value, "Next is null")
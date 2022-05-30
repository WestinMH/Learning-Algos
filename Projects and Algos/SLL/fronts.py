class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self, head):
        self.head = head

    # for my own ease in playing around I added a display the sll func
    def display(self):
        runner=self.head
        num = 1
        while runner != None:
            print(f"This is node {num} and its value is {runner.data}")
            num += 1
            runner=runner.next
        return self

    # for my own ease in playing around I added a function to add to the end of the sll
    def addTail(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self

    # simply return the value of the head node
    def front(self):
        if self.head == None:
            return None
        return self.head.data
    
    # remove the head node and return the sllist with the new head node
    def removeFront(self):
        if self.head ==  None:
            return None
        self.head = self.head.next
        return self.head.data

    # accepts a value and assigns it to be the new head node
    def addFront(self, value):
        newNode =  Node(value)
        if not self.head:
            self.head = newNode
            return self
        newNode.next = self.head
        self.head = newNode
        return self.head #the assignment said return a pointer to the head?
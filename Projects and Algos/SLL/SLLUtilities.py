class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    

class SLL:
    def __init__(self, head):
        self.head = head
    
    def add(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self
        
    # adds up all the values of the nodes in sll and returns the sum
    def findSum(self):
        runner=self.head
        sum=0
        while runner != None:
            sum+=runner.data
            runner=runner.next
        return sum

    # function searches for the given value in the list. I found return true, else false
    def findValue(self, value):
        runner=self.head
        while runner != None:
            if value == runner.data:
                return True
            runner=runner.next
        return False

    # returns the number of nodes in the sll
    def findLength(self):
        runner=self.head
        length = 0
        while runner != None:
            length += 1
            runner=runner.next
        return length

    # displays the sll nicely so it can be easily read
    def display(self):
        runner=self.head
        num = 1
        while runner != None:
            print(f"This is node {num} and its value is {runner.data}")
            num += 1
            runner=runner.next
        return self

# standalone function that moves the minimun value to the back of the sll
def minToFront(list):
    runner=list.head
    minimum_node = runner
    previous_node = None
    while runner.next:
        if minimum_node.data > runner.next.data:
            minimum_node = runner.next
            previous_node = runner
        runner=runner.next
    if previous_node:
        previous_node.next = minimum_node.next
    minimum_node.next = list.head
    list.head = minimum_node 
    return list

# standalone function that moves the maximun value to the back of the sll
def maxToBack(list):
    runner=list.head
    max_node = list.head
    previous_node = None
    while runner.next:
        if max_node.data < runner.next.data:
            max_node = runner.next
            previous_node = runner
        runner=runner.next
    if previous_node and max_node.next != None:
        previous_node.next = max_node.next
    runner.next = max_node
    if list.head == max_node:
        list.head = list.head.next
    max_node.next = None
    return list



# sll = SLL(Node(22))
# sll.add(66).add(222).add(2).add(1000).add(999)
# print(sll.head.next.data)
# print(SLL.findSum(sll))
# print(SLL.findValue(sll, 67))
# print(f"The length of this train is {SLL.findLength(sll)}")
# SLL.display(sll)
# SLL.display(minToFront(sll))
# SLL.display(maxToBack(sll))


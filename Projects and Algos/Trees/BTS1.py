


class BTNode :
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class BST:
    def __init__(self):
        self.root = None

    # add new  value to the BST at the correct location
    def add(self,value):
        if(self.root):
            runner = self.root
            while(runner):
                if(value>runner.value):
                    if(runner.right):
                        runner = runner.right
                    else:
                        runner.right = BTNode(value)
                        return self
                else:
                    if(runner.left):
                        runner = runner.left
                    else:
                        runner.left = BTNode(value)
                        return self
        self.root = BTNode(value)
        return self

    # check if the BST contains given value return true is so, else false
    def contains(self,data):
        if self.root:
            runner = self.root
            while runner:
                if data == runner.value:
                    return True
                if data < runner.value:
                    if not runner.left:
                        return False
                    runner = runner.left
                else:
                    if not runner.right:
                        return False
                    runner = runner.right
            return False

    # Create a min() method on the BST class that returns the smallest value found in the BST.
    def min(self):
        if not self.root:
            return "there are no values in this building!"
        runner = self.root
        while runner:
            runner = runner.left
            if runner.left == None:
                return f'the min value is {runner.value}'

    # Create a max() BST method that returns the largest value contained in the binary search tree.
    def max(self):
        if not self.root:
            return "there are no values in this building!"
        runner = self.root
        while runner:
            runner = runner.right
            if runner.right == None:
                return f'the max value is {runner.value}'

    # check of the BST is empty
    def isEmpty(self):
        if not self.root:
            return f'this is an empty BST'
        else:
            return f"this has got values"
        



# firstTree = BST()
# secondTree = BST()
# firstTree.add(45).add(15).add(57).add(11).add(102).add(9).add(77).add(2)
# print(firstTree.root.right.right.left.value)
# print(firstTree.contains(55))
# print(firstTree.min())
# print(firstTree.max())
# print(secondTree.isEmpty())

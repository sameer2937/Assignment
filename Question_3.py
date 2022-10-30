class Node():
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        if node.start < self.end:  #Replaced '<=' operator with '<'
            if not self.right_child:
                self.right_child = node
            return False            #removed one level of intendation as code wants to ommit false in all the situation
            #return self.left_child.insert(node) -----> #disabled this line of code
    
        elif node.end >= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)

class Calendar():
    def __init__(self):
        self.root: Node = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        return self.root.insert(node=Node(start, end))



calendar = Calendar()
print(calendar.book(5, 10)) # Expect True
print(calendar.book(8, 13)) # Expected False
print(calendar.book(10, 15)) #Expected True

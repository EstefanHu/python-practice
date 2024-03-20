class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def getValues(self):
        res = ''
        curr = self.head
        while curr != None:
            res += str(curr.value) + '->'
            curr = curr.next
        return res + 'Null'

    def addNode(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        return

    def addNodeAt(self, value, index):
        if index < 0:
            return
        newNode = Node(value)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        curr = self.head
        count = 1
        while curr.next and count < index:
            curr = curr.next
            count += 1
        newNode.next = curr.next
        curr.next = newNode
        return

    def popNode(self):
        curr = self.head
        if curr == None or curr.next == None:
            self.head = None
            return
        while curr.next.next:
            curr = curr.next
        curr.next = None
        return

    def checkIfLoop(self):
        s = self.head
        f = self.head.next
        while f and f.next.next:
            if s == f:
                return True
            s = s.next
            f = f.next.next
        return False

s = Solution()
s.addNode(1)
s.addNode(2)
s.addNode(3)
s.addNode(5)
s.addNode(8)
s.addNodeAt(4, 3)
s.addNodeAt(0, 0)
s.addNodeAt(7, 6)
s.addNodeAt(6, 6)
s.addNodeAt(9, 20)
s.addNodeAt(9, 20)
s.popNode()
print(s.getValues())
print(s.checkIfLoop())

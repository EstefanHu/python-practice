class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        def populate():
            self.addNode(23)
            self.addNode(61)
            self.addNode(9)
            self.addNode(45)
            self.addNode(14)
            self.addNode(90)
            self.addNode(31)
            self.addNode(82)
        populate()
        print('Initialized Linked List:')
        self.printValues()

    def printValues(self):
        res = ''
        curr = self.head
        while curr != None:
            res += str(curr.value) + '->'
            curr = curr.next
        print(res + 'None')

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


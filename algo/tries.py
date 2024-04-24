# Tries are great for word validation
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Trie:
    def __init__(self, name):
        self.name = name

trie = Trie('trie')

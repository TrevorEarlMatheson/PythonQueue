class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, key):
        self.values.insert(0, key)
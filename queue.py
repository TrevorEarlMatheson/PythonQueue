class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, key):
        self.values.append(key)
class Queue:
    def __init__(self):
        self.queue = []

    def Enqueue(self, key):
        self.queue.append(key)
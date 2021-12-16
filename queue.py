class Queue:
    def __init__(self):
        self.values = []

    # Add values to the end of the queue.
    def enqueue(self, key):
        self.values.append(key)

   # Remove value at the front of the queue.
    def dequeue(self):
        try:
            self.values.pop(0)
        finally:
            return

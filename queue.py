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

    # Reverse values in the queue
    def reverse_queue(self):
        end = len(self.values) - 1
        start = 0
        while start < end:
            temp = self.values[start]
            self.values[start] = self.values[end]
            self.values[end] = temp
            start += 1
            end -= 1
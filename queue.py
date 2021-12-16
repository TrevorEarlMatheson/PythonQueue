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

    # Interleave first half with second half.
    def inerleave_queue(self):
        if len(self.values) % 2 == 0:
            firstStart = 0
            firstEnd = (len(self.values) / 2) - 1
            secondStart = firstEnd + 1
            secondEnd = len(self.values) - 1
            while(firstStart <= firstEnd and secondStart <= secondEnd):
                temp = firstStart
                firstStart = secondStart
                secondStart = temp
                firstStart += 1
                secondStart += 1

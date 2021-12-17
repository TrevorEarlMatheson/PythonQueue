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
    def interleave_queue(self):
        try:
            if len(self.values) % 2 == 0:
                firstStart = 0
                firstEnd = int((len(self.values) / 2) - 1)
                secondStart = int((len(self.values) / 2))
                secondEnd = int(len(self.values) - 1)
                while (firstStart <= firstEnd and secondStart <= secondEnd):
                    temp = self.values[firstStart]
                    self.values[firstStart] = self.values[secondStart]
                    self.values[secondStart] = temp
                    firstStart += 1
                    secondStart += 1
            else:
                firstStart = 0
                firstEnd = int(((len(self.values) - 1) / 2) - 1)
                secondStart = firstEnd + 2
                secondEnd = len(self.values) - 1
                while (firstStart <= firstEnd and secondStart <= secondEnd):
                    temp = self.values[firstStart]
                    self.values[firstStart] = self.values[secondStart]
                    self.values[secondStart] = temp
                    firstStart += 1
                    secondStart += 1
        finally:
            return

    # Method sorts queue in ascending order.
    def ascending_sort(self):
        if self.values == []:
            return

        upperBound = len(self.values) - 1
        while upperBound >= 0:
            indexPosition = 0
            currentMin = None
            while indexPosition <= upperBound:
                if currentMin == None:
                    currentMin = indexPosition
                    indexPosition += 1
                elif self.values[currentMin] > self.values[indexPosition]:
                    currentMin = indexPosition
                    indexPosition += 1
                else:
                    indexPosition += 1
            self.enqueue(self.values.pop(currentMin))
            upperBound -= 1

    # Method sorts queue in descending order.
    def descending_sort(self):
        if self.values == []:
            return

        upperBound = len(self.values) - 1
        while upperBound >= 0:
            indexPosition = 0
            currentMax = None
            while indexPosition <= upperBound:
                if currentMax == None:
                    currentMax = indexPosition
                    indexPosition += 1
                elif self.values[currentMax] < self.values[indexPosition]:
                    currentMax = indexPosition
                    indexPosition += 1
                else:
                    indexPosition += 1
            self.enqueue(self.values.pop(currentMax))
            upperBound -= 1
import unittest
from queue_object import Queue

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        values = [3, 2, 5, 4, 7, 1, 5]
        for value in values:
            queue.enqueue(value)
        self.assertEqual(values, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(values))

    def test_dequeue(self):
        queue = Queue()
        values = [3, 2, 5, 4, 7, 1, 5]
        for value in values:
            queue.enqueue(value)
        self.assertEqual(values, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(values))
        queue.dequeue()
        values.pop(0)
        self.assertEqual(values, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(values))

    def test_dequeue_two(self):
        queue = Queue()
        expected = []
        queue.dequeue()
        self.assertEqual(expected, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(expected))

    def test_dequeue_three(self):
        queue = Queue()
        queue.enqueue(0)
        self.assertEqual([0], queue.values, "Queue was " + str(queue.values) + " but should have been " + str([0]))
        queue.dequeue()
        self.assertEqual([], queue.values, "Queue was " + str(queue.values) + " but should have been " + str([]))

    def test_reverse_queue_one(self):
        queue = Queue()
        values = [2, 5, 6, 8, 1, 3, 4, 0]
        for value in values:
            queue.enqueue(value)
        queue.reverse_queue()
        self.assertEqual(values[::-1], queue.values, "Queue was " + str(queue.values) + " but should have been " + str(values[::-1]))

    def test_reverse_queue_two(self):
        queue = Queue()
        queue.enqueue(0)
        queue.reverse_queue()
        self.assertEqual([0], queue.values, "Queue was " + str(queue.values) + " but should have been " + str([0]))

    def test_reverse_queue_three(self):
        queue = Queue()
        queue.reverse_queue()
        self.assertEqual([], queue.values, "Queue was " + str(queue.values) + " but should have been " + str([]))

    def test_interleave_queue_one(self):
        expectedResult = [4, 1]
        queue = Queue()
        values = [1, 4]
        for value in values:
            queue.enqueue(value)
        queue.interleave_queue()
        self.assertEqual(expectedResult, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(expectedResult))

    def test_interleave_queue_two(self):
        expectedResult = [1, 3, 4]
        queue = Queue()
        values = [4, 3, 1]
        for value in values:
            queue.enqueue(value)
        queue.interleave_queue()
        self.assertEqual(expectedResult, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(expectedResult))

    def test_interleave_queue_three(self):
        expectedResult = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]
        queue = Queue()
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for value in values:
            queue.enqueue(value)
        queue.interleave_queue()
        self.assertEqual(expectedResult, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(expectedResult))

    def test_interleave_queue_four(self):
        expectedResult = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        queue = Queue()
        values = [6, 7, 8, 9, 5, 1, 2, 3, 4]
        for value in values:
            queue.enqueue(value)
        queue.interleave_queue()
        self.assertEqual(expectedResult, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(expectedResult))

    def test_interleave_queue_five(self):
        expectedResult = []
        queue = Queue()
        queue.interleave_queue()
        self.assertEqual(expectedResult, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(expectedResult))

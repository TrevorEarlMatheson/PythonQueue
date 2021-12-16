import unittest
from queue import Queue

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
        queue.dequeue()
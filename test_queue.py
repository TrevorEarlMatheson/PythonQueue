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
        expected = []
        queue.dequeue()
        self.assertEqual(expected, queue.values, "Queue was " + str(queue.values) + " but should have been " + str(expected))

    def test_dequeue_three(self):
        queue = Queue()
        queue.enqueue(0)
        self.assertEqual([0], queue.values, "Queue was " + str(queue.values) + " but should have been " + str([0]))
        queue.dequeue()
        self.assertEqual([], queue.values, "Queue was " + str(queue.values) + " but should have been " + str([]))

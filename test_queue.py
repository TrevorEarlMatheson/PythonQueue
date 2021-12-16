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
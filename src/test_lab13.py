
# Імпортуйте вашу функцію/клас з файлу src.lab13
from src.lab13 import *


# -- Початок прикладу --
#
# class TestCalculateArea(unittest.TestCase):
#   """
#   Тести для функції calculate_area.
#   """
#   def test_positive_side(self):
#     """
#     Перевірка обчислення площі для додатного значення сторони.
import unittest
from lab13 import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_new_queue_is_empty(self):
        self.assertTrue(self.q.is_empty())
        self.assertEqual(len(self.q), 0)

    def test_enqueue_size(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.assertEqual(self.q.size(), 2)
        self.assertFalse(self.q.is_empty())

    def test_dequeue_order(self):
        for x in (1, 2, 3):
            self.q.enqueue(x)
        self.assertEqual(self.q.dequeue(), 1)
        self.assertEqual(self.q.dequeue(), 2)
        self.assertEqual(self.q.dequeue(), 3)
        self.assertTrue(self.q.is_empty())

    def test_peek_does_not_dequeue(self):
        self.q.enqueue(10)
        self.q.enqueue(20)
        self.assertEqual(self.q.peek(), 10)
        self.assertEqual(self.q.size(), 2)

    def test_peek_after_dequeue(self):
        self.q.enqueue(10)
        self.q.enqueue(20)
        self.q.dequeue()
        self.assertEqual(self.q.peek(), 20)

    def test_dequeue_empty_raises(self):
        with self.assertRaises(IndexError):
            self.q.dequeue()

    def test_peek_empty_raises(self):
        with self.assertRaises(IndexError):
            self.q.peek()

    def test_dequeue_until_empty_then_error(self):
        self.q.enqueue(1)
        self.q.dequeue()
        with self.assertRaises(IndexError):
            self.q.dequeue()

    def test_mixed_operations(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.assertEqual(self.q.dequeue(), 1)
        self.q.enqueue(3)
        self.assertEqual(self.q.peek(), 2)
        self.assertEqual(self.q.size(), 2)

    def test_none_and_mixed_types(self):
        self.q.enqueue(None)
        self.q.enqueue([1, 2])
        self.assertIsNone(self.q.dequeue())
        self.assertEqual(self.q.dequeue(), [1, 2])

    def test_large_number_of_elements(self):
        for i in range(1000):
            self.q.enqueue(i)
        for i in range(1000):
            self.assertEqual(self.q.dequeue(), i)
        self.assertTrue(self.q.is_empty())



if __name__ == '__main__':
    unittest.main()
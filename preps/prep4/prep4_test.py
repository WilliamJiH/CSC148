import prep4 as p4
from adts import *
import unittest
class test_stack(unittest.TestCase):
    def test_peek_none(self):
        stack = Stack()
        expect = None
        actural = p4.peek(stack)
        self.assertEqual(expect, actural, "The None should be returned")

    def test_one_element(self):
        stack = Stack()
        stack.push(3)
        expect = 3
        actural = p4.peek(stack)
        self.assertEqual(expect, actural, "The None should return 3")

    def test_multiple_elements(self):
        stack = Stack()
        stack.push(1)
        stack.push(3)
        stack.push("a")
        stack.push("d")
        expect = "d"
        actural = p4.peek(stack)
        self.assertEqual(expect, actural, "The function should return d")

    def test_reverse_two(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        p4.reverse_top_two(stack)
        expect = [1,2]
        actural = []
        actural.append(stack.pop())
        actural.append(stack.pop())
        self.assertEqual(expect, actural)

    def test_reverse_two_multiple_elements(self):
        stack = Stack()
        stack.push("a")
        stack.push("b")
        stack.push("c")
        p4.reverse_top_two(stack)
        expect = ['b','c']
        actural = []
        actural.append(stack.pop())
        actural.append(stack.pop())
        self.assertEqual(expect, actural)

    def test_reverse_two_multiple_elements_2(self):
        stack = Stack()
        stack.push("a")
        stack.push("b")
        stack.push("c")
        stack.push("d")
        stack.push(1)
        p4.reverse_top_two(stack)
        expect = ["d", 1]
        actural = []
        actural.append(stack.pop())
        actural.append(stack.pop())
        self.assertEqual(expect, actural)


class test_queue(unittest.TestCase):
    def test_remove_all_empty(self):
        queue = Queue()
        p4.remove_all(queue)
        expect = True
        actural = queue.is_empty()
        self.assertEqual(expect, actural)

    def test_remove_all_one_element(self):
        queue = Queue()
        queue.enqueue(1)
        p4.remove_all(queue)
        expect = True
        actural = queue.is_empty()
        self.assertEqual(expect, actural)

    def test_remove_all_2(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        p4.remove_all(queue)
        expect = True
        actural = queue.is_empty()
        self.assertEqual(expect, actural)

    def test_remove_but_last_one(self):
        queue = Queue()
        queue.enqueue(1)
        p4.remove_all_but_one(queue)
        expect = 1
        actural = queue.dequeue()
        self.assertEqual(expect, actural)

    def test_remove_but_last_one_multiple_elements(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        p4.remove_all_but_one(queue)
        expect = 4
        actural = queue.dequeue()
        self.assertEqual(expect, actural)
if __name__ == "__main__":
    unittest.main(exit = False)

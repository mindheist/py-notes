# Problem: Implement a fixed-capacity queue

# Data storage is in a list
# This list is fixed size - you cannot modify it after initialization


#
#  at least implement enqueue and dequeue

out <--- 1 <-- 2 <-- in
import mutex
import unittest
class Queue:
    def __init__(self,n):
        self.queue_list = [Null]*n
        #self.size = 0
        self.size = -1 # fill up till index
        my_mutex = mutex()

    def enqueue(self,key):
        my_mutex.acquire()
        if self.size+1 == n:
            return ERROR
        else:
            self.queue_list[self.size+1] = key
            self.size+=1
        my_mutex.release()
        # O(1)

    def dequeue(self):
        my_mutex.acquire()
        if self.size == -1:
            return "ERROR"
        else:
            return self.queue_list[0]

        #left shift all list elements
        for i in xrange(self.size):
            self.size[i] = self.size[i+1]
        self.size-=1
        my_mutex.release()

        #O(n) , n is the point to which it is filled

    def size(self):
        return self.size




class TestQueue(unittest.TestCase):
   my_queue = Queue(n)

   def test_create_queue(self):
       self.assertEqual(len(self.my_queue),n))

   # dequeue from empty Q

   def test_dequeue(self):
       self.asserEqual(self.my_queue.dequeue(),"ERROR")

   def test_enqueue(self):
       self.assertEqual(self.my_queue.enqueue("A"),self.my_queue[0])

   def test_size_1(self):
       self.assertEqual(self.my_queue.size(),0)

   def test_enqueue_2(self):
       self.assertEqual(self.my_queue.enqueue("B"),self.my_queue[1])

   def test_size_2(self):
       self.assertEqual(self.my_queue.size(),1)

   def test_dequeue_1(self):
       self.assertEqual(self.my_queue.dequeue(),"A")
       self.assertEqual(self.my_queue.size(),1)

   def test_dequeue_2(self):
       self.assertEqual(self.my_queue.dequeue(),"B")
       self.assertEqual(self.my_queue.size(),0)

   # enqueue on a full queue and expect an error.


if __name__ == "__main__":
   unittest.main()

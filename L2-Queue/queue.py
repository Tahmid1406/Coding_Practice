"""
In queue we have to support two things, inque and deque both in O(1) time complexity.
we use deque here because append and pop have nearly O(1) time complexity in this data structure
for append we have appnd() and appendleft()
for pop, we have pop() and popleft()
all of this have O(1) time complaxity

"""

from collections import deque

class Queue(object):
  def __init__(self) -> None:
    self.values = deque()

  def enqueue(self, x:int) -> None:
    self.values.append(x)

  def dequeue(self) -> int:
    return self.values.popleft()

q = Queue()
for x in range(5):
  q.enqueue(x)

print(q.values)

q.dequeue()
q.dequeue()

print(q.values)
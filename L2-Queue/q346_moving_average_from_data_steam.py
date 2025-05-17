"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Implement the MovingAverage class:
MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

"""

class MovingAverage(object):
  # we need a queue with capacity of size
  def __init__(self, size:int) -> None:
    self.values = deque()
    self.capacity = size

  def next(self, val:int) -> float:
    if len(self.values) == self.capacity:
      self.values.popleft()
    self.values.append(val)

    return sum(self.values) / len(self.values) # summing here causes O(n) complexity
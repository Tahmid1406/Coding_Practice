"""

The MaxStack Problem
The problem asks us to design a customized stack structure, which is a common Last-In-First-Out (LIFO) data structure with an added capability of retrieving and removing the maximum element it contains. This stack should support the following operations:

push(x): Add an element x to the top of the stack.
pop(): Remove the element at the top of the stack and return it.
top(): Return the element at the top of the stack without removing it.
peekMax(): Retrieve the maximum element in the stack without removing it.
popMax(): Retrieve the maximum element in the stack and remove it. If there are multiple instances of the maximum element, only the top-most one should be removed.
The challenge lies in designing these operations to be time efficient, specifically requiring the top call to be O(1) and all other calls to be O(log n) complexity.

""""

class MaxStack(object):
  def __init__(self) -> None:
    self.pairs = []

  def push(self, val:int) -> None:
    if len(self.pairs) == 0:
      pair = [val, 0]
    else:
      index_of_max = self.pairs[-1][1]
      max_item = self.pairs[index_of_max][0]

      if val > max_item:
        index_of_max = len(self.pairs)
      pair = [val, index_of_max]

    self.pairs.append(pair)

  def pop(self) -> None:
    v = self.pairs[-1][0]
    self.pairs.pop()
    return v

  def top(self) -> int:
    v = self.pairs[-1][0]
    return v

  def peekMax(self) -> int:
    index_of_max = self.pairs[-1][1]
    v = self.pairs[index_of_max][0]
    return v

def popMax(self) -> int:
  #get the max value
  index_of_max_value = self.pairs[-1][1]
  return_value = self.pairs[index_of_max_value][0]

  # adjust the indexes after it
  if index_of_max_value == 0:
    max_value = -float('inf')
    max_index = -1
  else:
    max_value, max_index = self.pairs[index_of_max_value-1]
    for index in range(index_of_max_value+1, len(self.pairs)):
      val = self.pairs[index][0]
      if val > max_value:
        max_value = val
        max_index = index-1 # since we will pop one element later
        self.pairs[index][1] = max_index

  # pop the max
  self.pairs.pop(index_of_max_value)

  return return_value





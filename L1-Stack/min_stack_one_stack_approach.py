class MinStack_One_Stack(object):
  def __init__(self) -> None:
    self.pairs = []

  def push(self, val:int) -> None:
    if len(self.pairs) == 0:
      pair = (val, val) # pair of (val, min_value)
    else:
      old_min_val = self.pairs[-1][1]
      new_min_val = min(val, old_min_val)
      pair = (val, new_min_val)

    self.pairs.append(pair)

  def pop(self) -> None:
    self.pairs.pop()

  def top(self) -> int:
    return self.pairs[-1][0]

  def getMin(self) -> None:
    return self.pairs[-1][1]


if __name__ == "__main__":
    test_stack = MinStack_One_Stack()

    for v in range(10):
    test_stack.push(v)

    test_stack.push(-10)
    test_stack.push(-2)
    test_stack.push(-1)
    test_stack.push(-1)
    test_stack.push(-5)


    test_stack.pop()
    test_stack.pop()
    test_stack.pop()

    print(test_stack.top())
    print(test_stack.getMin())
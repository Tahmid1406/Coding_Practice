class MinStack(object):
  def __init__(self):
    self.values = []
    self.min_values = []
    

  def push(self, val:int) -> None:
    self.values.append(val)

    if len(self.min_values) == 0:
      min_value = val
    else: 
      old_min_value = self.min_values[-1]
      new_min_value = min(val, old_min_value)
      min_value = new_min_value

    self.min_values.append(min_value)


  def pop(self) -> None:
    if len(self.values) == 0:
      raise ValueError("error")
    else:
      self.values.pop()
      self.min_values.pop()


  def top(self) -> Optional[int]:
    if len(self.values) == 0:
      raise ValueError("Stack empty")
    else: 
      return self.values[-1]


  def getMin(self) -> Optional[int]:
    if len(self.min_values) == 0:
      raise ValueError("Stack empty")
    else: 
      return self.min_values[-1]

def main():
    s_min = MinStack()
    for v in range(10):
        s_min.push(v)

    s_min.push(-10)
    s_min.push(-2)
    s_min.push(-1)
    s_min.push(-1)
    s_min.push(-5)

    s_min.pop()
    s_min.pop()
    s_min.pop()

    print("Top of stack:", s_min.top())
    print("Current minimum:", s_min.getMin())


if __name__ == "__main__":
    main()
from typing import Optional

class Stack(object): 
  def __init__(self) -> None:
    self.array = []

  def push(self, x: int) -> None:
    self.array.append(x)

  def pop(self) -> Optional[int]: #we might not return an int in case the stack is empty
    if len(self.array) == 0: 
      raise ValueError("You can not remove an element from an empty stack")
    else:
      v = self.array.pop()
      return v


s = Stack()
for v in range(5):
  s.push(v)

print(s.array)

for _ in range(2): 
  s.pop()

print(s.array)
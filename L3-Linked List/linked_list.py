class ListNode(object):
  def __init__(self, key:int) -> None:
    self.key = key
    self.prev = None
    self.next = None

  def __str__(self) -> str:
    s = f"[{self.key}]"
    return s


class LinkedList(object):
  def __init__(self) -> None:
    self.head = None

  def insert(self, x:ListNode) -> None:
    x.next = self.head
    if self.head:
      self.head.prev = x
    self.head = x
    x.prev = None

  def delete(self, x:ListNode) -> None:
    if x.prev:
      x.prev.next = x.next
    else:
      self.head = x.next
    if x.next:
      x.next.prev = x.prev

  def __str__(self) -> str:
    nodes = []
    x = self.head
    while x:
      nodes.append(x)
      x = x.next
    return " <--> ".join([str(node) for node in nodes])


dll = LinkedList()


for v in range(5,10):
  node = ListNode(v)
  dll.insert(node)

print(str(dll))  
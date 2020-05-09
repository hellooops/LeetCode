class MyStack:
  def __init__(self):
    self._data = []

  def push(self, obj) -> None:
    self._data.append(obj)

  def pop(self):
    if self.empty():
      return -1

    popVal = self._data[-1]
    del self._data[-1]
    return popVal

  def size(self) -> int:
    return len(self._data)

  def empty(self) -> bool:
    return self.size() <= 0

  def __str__(self) -> str:
    return f"<MyStack {self._data}>"

  def __repr__(self) -> str:
    return str(self)


if __name__ == '__main__':
  stack = MyStack()
  stack.push(1)
  print(stack)
  print(stack.pop())
  print(stack)
  print(stack.empty())
  stack.push(1)
  stack.push(2)
  print(stack.empty())
  print(stack.size())
  print(stack.pop())
  print(stack.pop())
  print(stack.pop())
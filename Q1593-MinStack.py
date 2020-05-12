__author__ = "dericl"
__email__ = "slxs1415@163.com"

"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
"""


class MinStack:
  def __init__(self):
    self._data = []
    self._minItems = []

  def push(self, x: int) -> None:
    self._data.append(x)
    if not self._minItems:
      self._minItems.append(x)
    else:
      if x <= self._minItems[-1]:
        self._minItems.append(x)

  def pop(self) -> None:
    if self.size() <= 0:
      return

    self._removeMin(self._data[-1])
    del self._data[-1]


  def top(self) -> int:
    if self.size() <= 0:
      return -1

    return self._data[-1]

  def getMin(self) -> int:
    if not self._minItems:
      raise

    return self._minItems[-1]

  def size(self) -> int:
    return len(self._data)

  def _removeMin(self, x: int) -> None:
    if not self._minItems:
      return

    if self._minItems[-1] == x:
      del self._minItems[-1]

  def __str__(self) -> str:
    return str(self._data)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

if __name__ == '__main__':
  minStack = MinStack()
  print(minStack)
  minStack.push(-2)
  print(minStack)
  minStack.push(0)
  print(minStack)
  minStack.push(-3)
  print(minStack)
  print(minStack.getMin())
  print(minStack)
  minStack.pop()
  print(minStack)
  print(minStack.top())
  print(minStack)
  print(minStack.getMin())
  print(minStack)
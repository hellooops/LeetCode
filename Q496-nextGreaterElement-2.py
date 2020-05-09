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

  def peek(self):
    if self.empty():
      return -1
    return self._data[-1]

  def __str__(self) -> str:
    return f"<MyStack {self._data}>"

  def __repr__(self) -> str:
    return str(self)


class Solution:
  def nextGreaterElement(self, nums1, nums2):
    m = dict()
    stack = MyStack()
    for i in nums2:
      while not stack.empty() and i > stack.peek():
        m[stack.pop()] = i
      stack.push(i)
    while not stack.empty():
      m[stack.pop()] = -1

    ret = []
    for i in nums1:
      ret.append(m[i])
    return ret


if __name__ == '__main__':
  nums1 = [4, 1, 2]
  nums2 = [1, 3, 4, 2]
  print(Solution().nextGreaterElement(nums1, nums2))
  nums1 = [2, 4]
  nums2 = [1, 2, 3, 4]
  print(Solution().nextGreaterElement(nums1, nums2))
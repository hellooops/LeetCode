class Solution:
  def nextGreaterElement(self, nums1, nums2):
    ret = []
    for num1 in nums1:
      for num2Idx in range(nums2.index(num1), len(nums2)):
        if nums2[num2Idx] > num1:
          ret.append(nums2[num2Idx])
          break
      else:
        ret.append(-1)
    return ret


if __name__ == '__main__':
  nums1 = [4, 1, 2]
  nums2 = [1, 3, 4, 2]
  print(Solution().nextGreaterElement(nums1, nums2))

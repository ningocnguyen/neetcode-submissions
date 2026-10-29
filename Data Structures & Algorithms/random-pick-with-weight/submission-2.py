import random
from typing import List


class Solution:

  def __init__(self, w: List[int]):
    self.prefix_sum = []
    self.current = 0
    for n in w:
      self.current += n
      self.prefix_sum.append(self.current)

  def pickIndex(self) -> int:
    target = random.randint(1, self.current)
    l, r = 0, len(self.prefix_sum) - 1

    while l <= r:
      mid = (l + r) // 2
      if target == self.prefix_sum[mid]:
        return mid
      elif target < self.prefix_sum[mid]:
        r = mid - 1
      else:
        l = mid + 1

    return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
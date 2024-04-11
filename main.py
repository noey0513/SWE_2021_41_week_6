from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
  ans1=0
  ans2=0
  for i, ele1 in enumerate(nums):
    for j, ele2 in enumerate(nums):
      if i != j:
        if ele1+ele2 == target:
          return [i,j]
  return []
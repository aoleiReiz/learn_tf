from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")
        for num in nums:
            if num >= first:
                if num == first:
                    continue
                third = second
                second = first
                first = num
            elif num >= second:
                if num == second:
                    continue
                third = second
                second = num
            elif num > third:
                third = num
        return first if third == float("-inf") else third


if __name__ == '__main__':
    s = Solution()
    arrs = [
        [3, 2, 1],
        [1, 2],
        [2,2,3,1]
    ]
    for arr in arrs:
        print(s.thirdMax(arr))
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(track: List):
            if len(track) == len(nums):
                ans.append(list(track))
                return
            for num in nums:
                if num in track:
                    continue
                track.append(num)
                helper(track)
                track.pop()
        helper([])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def helper(arr, left, right):
            while left < right:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1
        n = len(s)
        s_arr = [i for i in s]
        for i in range(0, n, 2*k):
            if n - i < k:
                helper(s_arr, i, n-1)
            elif k <= n - i < 2*k:
                helper(s_arr, i, i + k - 1)
            else:
                helper(s_arr, i, i + k - 1)
        return "".join(s_arr)

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split("-"))
        n = len(s)
        if k >= n:
            return s.upper()
        j = n - k
        ans = []
        while j >= 0:
            ans.append(s[j: j+k].upper())
            j -= k
        if j > -k:
            ans.append(s[:j+k].upper())
        return  "-".join(ans[::-1])


if __name__ == '__main__':
    solution = Solution()
    S = "5F3Z-2e-9-w"
    K = 4
    print(solution.licenseKeyFormatting(S,K))

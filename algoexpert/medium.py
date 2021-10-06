def threeNumberSum(array, targetSum):
    def twoSum(arr, target):
        left = 0
        right = len(arr) - 1
        ret = []
        while left < right:
            if arr[left] + arr[right] == target:
                ret.append([arr[left], arr[right]])
                left += 1
                right -= 1
            elif arr[left] + arr[right] > target:
                right -= 1
            else:
                left += 1
        return ret
    ans = []
    array = sorted(array)
    for i in range(len(array)):
        two_sum_res = twoSum(array[i+1:], targetSum - array[i])
        for r in two_sum_res:
            ans.append([array[i], *r])
    return ans

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    min_dist = float("inf")
    ans = []
    for num1 in arrayOne:
        for num2 in arrayTwo:
            dist = abs(num2 - num1)
            if dist < min_dist:
                ans = [num1, num2]
                min_dist = dist
    return ans


def smallestDifference2(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    idxOne = 0
    idxTwo = 0
    current = float("inf")
    smallest = float("inf")
    ans = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            firstNum += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            secondNum += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            ans = [firstNum, secondNum]
    return ans


def spiralTraverse(array):
    # Write your code here.
    row_start = 0
    row_end = len(array) - 1
    col_start = 0
    col_end = len(array[0]) - 1
    ans = []
    while row_start <= row_end and col_start <= col_end:
        for col in range(col_start, col_end + 1):
            ans.append(array[row_start][col])
        for row in range(row_start + 1, row_end + 1):
            ans.append(array[row][col_end])
        for col in reversed(range(col_start, col_end)):
            if row_start == row_end:
                break
            ans.append(array[row_end][col])
        for row in reversed(range(row_start + 1, row_end)):
            if col_start == col_end:
                break
            ans.append(array[row][col_start])

        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1
    return ans


def arrayOfProducts(array):
    # Write your code here.
    left_dp = [1]
    right_dp = [1]
    n = len(array)
    for i in range(1, n):
        left_dp.append(left_dp[-1] * array[i-1])
    for i in range(n-2, -1, -1):
        right_dp.append(right_dp[-1] * array[i+1])
    ans = []
    for i in range(n):
        ans.append(left_dp[i] * right_dp[n - i - 1])
    return ans

def firstDuplicateValue(array):
    # Write your code here.
    d = {}
    for num in array:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    for num in array:
        if d[num] == 1:
            return num
    return -1




if __name__ == '__main__':
    array = [12,3,1,2,-6,5,-8,6]
    print(arrayOfProducts([5, 1, 4, 2]))

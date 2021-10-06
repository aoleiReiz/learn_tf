def longestPeak(array):
    n = len(array)
    i = 1
    ans = 0
    while i < n - 1:
        is_peak = array[i-1] < array[i] > array[i+1]
        if not is_peak:
            i += 1
            continue
        left_index = i - 2
        while left_index >=0 and array[left_index] < array[left_index + 1]:
            left_index -= 1
        right_index = i + 2
        while right_index < n and array[right_index] < array[right_index + 1]:
            right_index += 1
        ans = max(ans, right_index - left_index - 1)
        i = right_index
    return ans


if __name__ == '__main__':
    array1 = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(array1))

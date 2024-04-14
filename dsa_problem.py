
def max_subarray(arr: list[int]):
    len_arr = len(arr)
    if len_arr == 1:
        return arr
    max_sum = 0

    for i in range(0, len_arr - 1):
        sub_array_sum = 0
        for j in range(i + 1, len_arr):
            sub_array_sum += arr[j]
            if sub_array_sum > max_sum:
                max_sum = sub_array_sum

    return max_sum

def max_min_divide_conquer(arr, low, high):
    class Pair:
        def __init__(self):
            self.max = 0
            self.min = 0

    result = Pair()

    if low == high: #incase of 1 element
        result.max = arr[low]
        result.min = arr[low]
        return result

    if high == low + 1:#incase of two elements
        if arr[low] < arr[high]:
            result.min = arr[low]
            result.max = arr[high]
        else:
            result.min = arr[high]
            result.max = arr[low]
        return result

    mid = (low + high) // 2
    left = max_min_divide_conquer(arr, low, mid)
    right = max_min_divide_conquer(arr, mid + 1, high)

    result.max = max(left.max, right.max)
    result.min = min(left.min, right.min)

    return result

arr = [6, 4, 26, 14, 33, 64, 46]
result = max_min_divide_conquer(arr, 0, len(arr) - 1)
print("Maximum element is:", result.max)
print("Minimum element is:", result.min)

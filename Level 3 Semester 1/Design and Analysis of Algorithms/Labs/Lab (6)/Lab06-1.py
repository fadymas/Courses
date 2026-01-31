def binary_search_dc(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    print(f"low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_dc(arr, target, low, mid - 1) #search left side
    else:
        return binary_search_dc(arr, target, mid + 1, high) #search right side

arr = [3, 5, 7, 9, 11, 13, 15]
target = 13

index = binary_search_dc(arr, target, 0, len(arr) - 1)

if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found.")

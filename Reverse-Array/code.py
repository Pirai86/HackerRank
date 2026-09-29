arr = [1, 2, 3]


def reverseArray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[right], arr[left] = arr[left], arr[right]
        left += 1
        right -= 1

    return arr

print(reverseArray(arr))

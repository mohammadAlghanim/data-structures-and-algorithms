def insertShiftArray(arr, key):
  left = 0
  right = len(arr) - 1

  while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

  return -1


my_array = [4, 8, 15, 16, 23, 42]
inserted_array = insertShiftArray(my_array,15)
print(inserted_array)
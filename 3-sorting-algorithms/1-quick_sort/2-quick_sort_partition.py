def partition(arr, left_pointer, right_pointer):
    pivot = arr[left_pointer]
    pivot_index = left_pointer
    while left_pointer < right_pointer:
        while left_pointer < len(arr) and arr[left_pointer] <= pivot:
            left_pointer += 1
        while arr[right_pointer] > pivot:
            right_pointer -= 1
        if left_pointer < right_pointer:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
    arr[pivot_index], arr[right_pointer] = arr[right_pointer], arr[pivot_index]
    return right_pointer


def quick_sort(arr, start_index, end_index):
    if end_index > start_index:
        pivot_index = partition(arr, start_index, end_index)
        quick_sort(arr, start_index, pivot_index - 1)
        quick_sort(arr, pivot_index+1, end_index)
    return arr


to_sort = [10, 16, 2, 24, 15, 52, 13]

# print('Before Sort:')
# print(to_sort)
# print('After Sort')
print(quick_sort(to_sort, 0, len(to_sort) - 1))
print(quick_sort([2, 1], 0, 1))
print(quick_sort([], 0, 0))

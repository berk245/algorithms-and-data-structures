def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    values_smaller = []
    values_greater = []

    for value in arr:
        if value > pivot:
            values_greater.append(value)
        else:
            values_smaller.append(value)

    return quick_sort(values_smaller) + [pivot] + quick_sort(values_greater)


print(quick_sort([1, 4, 2, 3, 4, 1, 6, 7, 5]))

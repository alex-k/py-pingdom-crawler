def sort(a):
    if len(a) == 0:
        return a

    pivot = a[0]
    left = []
    right = []
    for element in a:
        if element < pivot:
            left.append(element)
        if element > pivot:
            right.append(element)

    return sort(left) + [pivot] + sort(right)

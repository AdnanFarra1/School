def InsertionSort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        ValueToSort = list_a[i]

        while list_a[i-1] > ValueToSort and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i-1
    return list_a

print(InsertionSort([2,43,5,2,5,63,5,3,5,3,56,3,456,435,6,53,452,13]))
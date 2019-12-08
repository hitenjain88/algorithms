def merge_sort(array):
    length = len(array)
    if length == 1:
        return array
    else:
        array1 = merge_sort(array[0:(length // 2)])
        array2 = merge_sort(array[(length // 2):])

        sorted_array = []
        length1 = len(array1)
        length2 = len(array2)
        index1 = 0
        index2 = 0
        while index1 < length1 and index2 < length2:
            if array1[index1] < array2[index2]:
                sorted_array.append(array1[index1])
                index1 += 1
            else:
                sorted_array.append(array2[index2])
                index2 += 1

        if index1 == length1:
            sorted_array.extend(array2[index2:])
        else:
            sorted_array.extend(array1[index1:])

        return sorted_array

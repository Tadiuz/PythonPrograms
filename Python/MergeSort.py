array = [1,9,2,8,3,4,5,6,7,65,34,23,231,34,54,56,76,78,98,768,5675,3452,3466,3567,235,12]




def merge_sort(array):
    if len(array) == 1:
        return array
    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])
    i , j = 0, 0
    temp = []
    for k in range(len(left) + len(right)): 
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                temp.append(left[i])
                i +=1
            else:
                temp.append(right[j])
                j +=1
        else:
            if i >= len(left):
                temp.extend(right[j:])
            else:
                temp.extend(left[i:])
            break

    return temp
                

#array = [1,2,3]

print(merge_sort(array))


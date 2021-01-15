def binarySearch(arr, value):
    arrLenght = len(arr)
    mid = int(arrLenght/2)
    if arrLenght == 1:
        return (arr[0] == value)
    else:
        if arr[mid] > value:
            newArr = arr[:mid]
        elif arr[mid] < value:
            newArr = arr[mid:]
        else:
            return True
        return binarySearch(newArr, value)



#We are looking for the value in the array
value = 91

#it is NOT a 0 to 99 list (some are missing) but it is sorted
arr = [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21,  23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 39, 40, 41, 42, 44, 45, 47, 48, 49, 51, 53, 54, 56, 57, 58, 59, 64, 67, 68, 69, 70, 71, 74, 75, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]


answer = binarySearch(arr, value);

print("Is there " + str(value) + " in the array : " + str(answer))
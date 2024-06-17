
# Sorting Algorithms:

# Bubble sort
# Quick sort
# Merge sort

students_age = [34, 22, 17, 123, 25, 16, 23344, 28, 24, 30]
           

def bubble_sort(alist):
    n = len(alist)

    for i in range(n):
        for j in range(n - i - 1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]   

    # return sorted(alist, reverse=True)
    return alist


# print(bubble_sort(students_age))


# print(len(students_age))
# print(students_age[8])
            

def bubble_sort2(alist):
    n = len(alist)
    has_swapped = True

    while (has_swapped):
        has_swapped = False
        for i in range(n -1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                has_swapped = True

    return alist

# print(bubble_sort2(students_age))





# Quick sort


views = [{'Travel to Rome': 2004}, {'Visiting Berlin': 1734}, ]

views_in_numbers = [2004, 1734, 562, 11, 7803, 114402, 77, 7803, 3330, 55508]

views2 = []

# print(len(views2))


def quick_sort(arr):  
    n = len(arr)
    if n <= 1:
        return arr

    select = arr[n // 2]
    # select = arr[0]

    left = [x for x in arr if x < select]   # [2004, 1734, 562, ....]
    middle = [x for x in arr if x == select] # [7803, 7803]
    right = [x for x in arr if x > select]  # [114402, 55508]
    # print('function called')

    return quick_sort(left) + middle + quick_sort(right)
    # return quick_sort(right) + middle + quick_sort(left)


# print(quick_sort(views_in_numbers))



# Searching Algorithms

# Linear search

prices = [22.34, 9.99, 55.23, 40, 101.88, 29.33] # target = 444

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 # not necessarily required
        

# print(linear_search(prices, 10))



prices = [22.34, 9.99, 55.23, 40, 101.88, 29.33] # target = 40


goals = [4, 8, 10, 14, 15, 18, 25, 28] # target = 8


def binary_search(arr, target):

    start_index = 0
    end_index = len(arr) - 1
    index = -1


    while (start_index <= end_index) and index == -1:
        middle_index = (start_index + end_index) // 2

        if arr[middle_index] == target:
            index = middle_index
            # return index
        else:
            if arr[middle_index] > target:
                end_index = middle_index -1
            elif arr[middle_index] < target:
                start_index = middle_index + 1

    return index


# print(binary_search(goals, 14))





mileages = [220, 450, 33, 170, 70, 300, 22, 280, 500, 120]

# [220], [450], [33], [], [170], [], [], [300]

# [33], [220], [450],

# [33, 220, 450]

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    middle_index = len(arr) // 2

    left_arr = arr[:middle_index]
    right_arr = arr[middle_index:]


    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):

    i = 0
    j = 0

    result = []

    while i < len(left_arr) and j < len(right_arr):

        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        elif left_arr[i] > right_arr[j]:
            result.append(right_arr[j])
            j += 1

    # result.extend(left_arr[i:])
    # result.extend(right_arr[j:])

    result += left_arr[i:]
    result += right_arr[j:]

    return result
        

print(merge_sort(mileages))


        














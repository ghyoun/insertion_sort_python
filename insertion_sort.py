import datetime
def insertion_sort(arr):
    for index in range(1, len(arr)):
        if (arr[index] < arr[index - 1]):
            remove = arr[index]
            lesser_index = index - 1
            while (remove < arr[lesser_index] and lesser_index >= 0):
                arr[lesser_index + 1] = arr[lesser_index]
                lesser_index = lesser_index - 1
            arr[lesser_index + 1] = remove

arr2 = [2605, 7917, 5425, 6578, 1778, 4144, 615, 5007, 3970, 1689, 9004, 7214, 8703, 6022, 272,
 2232, 9198, 9317, 9197, 9330, 642, 8875, 2715, 6619, 5374, 3496, 3405, 3808, 442, 9823, 5546,
 6411, 4302, 9483, 9294, 1672, 3852, 6604, 8846, 3780, 545, 18, 8965, 9307, 8522, 4668, 8403, 312,
 1733, 5061, 3651, 465, 4123, 4538, 9315, 5485, 2568, 5522, 1207, 2282, 7616, 320, 3812, 938, 2935,
 2986, 1621, 9443, 7769, 8320, 6320, 3035, 6687, 2971, 7374, 5088, 8404, 9614, 1678, 6735, 3829, 4629,
 4971, 5923, 1711, 6768, 504, 8895, 8206, 7489, 2170, 7883, 8871, 5206, 2632, 3345, 3906, 5347, 2169, 3975]

before = datetime.datetime.now()
insertion_sort(arr2)
after = datetime.datetime.now()
print arr2

print after.microsecond - before.microsecond, "ms"

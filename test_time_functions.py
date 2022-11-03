from unittest import result
import numpy as np


def checkTime(arr1, arr2):
    work_array = np.array(arr1)
    employ_array = np.array(arr2)

    # subtract the employer array from the worker array to see if there are any negative numbers
    result_array = np.subtract(work_array, employ_array)

    print(work_array.tolist())
    print("minus")
    print(employ_array.tolist())
    print("equals")
    print(result_array.tolist())

    # if there are any negative numbers, return false, otherwise return True
    if (-1 in result_array.tolist()):
        return False
    return True

# represents 9am - 5pm availability
worker_time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]

# represents 11am - 1pm requirement for the job
employer_time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0]

print(checkTime(worker_time, employer_time))

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]

#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1]
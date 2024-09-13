"""
input      : Two sorted arr1 - size m and arr2 - size n
output     : Merge Tow arrays into single sorted array

constraint : time complexity - O(m log m + n log n), space complexity - O(1)

"""

# Used Two pointer concept

# O(m log m + n log n)
def merge_two_arrs(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = m-1
    j = 0
    while i >= 0 and j < n:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1
        else:
            break
    arr1.sort()
    arr2.sort()

if __name__ == '__main__':
    test_cases = [
         [[1,3,5],[2,4,6]],
         [[10,12,14],[1,3,5]],
         [[2,3,8],[4,6,10]],
         [[1],[2]]
        ]
    test_case_5_arr1 = [i for i in range(1, 100001)]
    test_case_5_arr2 = [i for i in range(50001, 100001)]
    test_cases.append([test_case_5_arr1, test_case_5_arr2])

    solutions = [
         [[1,2,3],[4,5,6]],
         [[1,3,5],[10,12,14]],
         [[2,3,4],[6,8,10]],
         [[1],[2]]
        ]
    solution_case_5_arr1 = [i for i in range(1, 50001)]
    solution_case_5_arr2 = [i for i in range(50001, 100001)]
    solutions.append([solution_case_5_arr1, solution_case_5_arr2])
    for test_case, solution in zip(test_cases, solutions):
        arr1,arr2 = test_case
        merge_two_arrs(arr1,arr2)
        if arr1 != solution[0] or arr2 != solution[1]:
            print(f"Test case failed:")
        else:
            print(f"Test case passed:")
    
    

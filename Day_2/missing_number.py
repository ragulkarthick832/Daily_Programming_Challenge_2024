"""
input      : arr consisting of n-1 distinct integers
output     : missing integer

constraint : time complexity - O(N), space complexity - O(1)

"""

# Used Summation of n integers formula to find the missing number

# O(N)
def missing_number(arr):
    last_element = len(arr)+1
    summation = (last_element)*(last_element+1)/2
    array_sum = sum(arr)
    return summation - int(array_sum)

if __name__ == '__main__':
    test_cases = [[1,2,4,5],
                 [2,3,4,5],
                 [1,2,3,4],
                 [1]]
    test_case_5 = [i for i in range(1,1000000)]
    test_cases.append(test_case_5)
    solutions = [3,1,5,2,1000000]
    for test_case, solution in zip(test_cases, solutions):
        answer = missing_number(test_case)
        if answer != solution:
            print(f"Test case failed:")
        else:
            print(f"Test case passed:")
    
    

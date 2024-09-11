"""
input      : arr consisting of n+1 integers
output     : missing integer

constraint : time complexity - O(N), space complexity - O(1)

"""

# Used Summation of n integers formula to find the missing number

# O(N)
def missing_number(arr):
    last_element = len(arr)
    summation = (last_element)*(last_element+1)/2
    array_sum = sum(arr)
    difference = summation - int(array_sum)
    return  last_element - difference

if __name__ == '__main__':
    test_cases = [[1,3,4,2,2],
                 [3,1,3,4,2],
                 [1,1],
                 [1,4,4,2,3]]
    test_case_5 = [i for i in range(1,1000000)]
    test_case_5.append(50000)
    test_cases.append(test_case_5)
    solutions = [2,3,1,4,50000]
    for test_case, solution in zip(test_cases, solutions):
        answer = missing_number(test_case)
        print(answer)
        if answer != solution:
            print(f"Test case failed:")
        else:
            print(f"Test case passed:")
    
    

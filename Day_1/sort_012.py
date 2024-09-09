"""
input      : arr consisting only of 0s, 1s and 2s
output     : sorted arr

constraint : time complexity - O(N), space complexity - O(1)

"""

# Used Dutch National Flag Algorithm developed by Edsger Dijkstra

# O(N)
def sort_array(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for number in arr: # O(N)
        if number == 0:
            count_0 += 1
        elif number == 1:
            count_1 += 1
        else:
            count_2 += 1
    current_index = 0
    for i in range(count_0): # O(N)
        arr[current_index] = 0
        current_index += 1
        
    for i in range(count_1): # O(N)
        arr[current_index] = 1
        current_index += 1
        
    for i in range(count_2): # O(N)
        arr[current_index] = 2
        current_index += 1

if __name__ == '__main__':
    test_cases = [[0, 1, 2, 1, 0, 2, 1, 0],
                 [2, 2, 2, 2],
                 [0, 0, 0, 0],
                 [1, 1, 1, 1],
                 [2, 0, 1],
                 []]
    solutions = [[0, 0, 0, 1, 1, 1, 2, 2],
                [2, 2, 2, 2],
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 1, 2],
                []]
    for test_case, solution in zip(test_cases, solutions):
        sort_array(test_case)
        if test_case != solution:
            print(f"Test case failed: {test_case} != {solution}")
        else:
            print(f"Test case passed: {test_case} == {solution}")
    
    

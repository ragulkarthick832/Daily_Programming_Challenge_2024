"""
input      : arr - size n
output     : leader elements

constraint : time complexity - O(N), space complexity - O(N)

"""
# Traversing from right to left , keeping track of maximum element

# O(N)
def find_leader_elements(arr):
    n = len(arr)
    answer = []
    pointer = n-1
    max_element = arr[n-1] 
    answer.append(max_element) # Last element is always a leader
    for i in range(n-2,-1,-1):
        if arr[i] > max_element:
            answer.append(arr[i])
            max_element = arr[i]
            
    answer.reverse()
    return answer
        

if __name__ == '__main__':
    test_cases = [
         [1,2,3,4,0],
         [7,10,4,10,6,5,2],
         [5],
         [100,50,20,10]
        ]
    test_case_5 = [i for i in range(1, 1000001)]
    test_cases.append(test_case_5)

    solutions = [
         [4,0],
         [10,6,5,2],
         [5],
         [100,50,20,10],
         [1000000]
        ]
    for test_case, solution in zip(test_cases, solutions):
        answer = find_leader_elements(test_case)
        if answer != solution:
            print(f"Test case failed:")
        else:
            print(f"Test case passed:")
    
    

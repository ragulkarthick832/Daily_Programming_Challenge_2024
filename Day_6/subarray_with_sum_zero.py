def find_zero_sum_subarrays(arr):
    sum_map = {}
    cumulative_sum = 0
    result = []

    for i in range(len(arr)):
        cumulative_sum += arr[i]
        if cumulative_sum == 0:
            result.append((0, i))
        if cumulative_sum in sum_map:
            for start_index in sum_map[cumulative_sum]:
                result.append((start_index + 1, i))
        if cumulative_sum in sum_map:
            sum_map[cumulative_sum].append(i)
        else:
            sum_map[cumulative_sum] = [i]

    return result

if __name__ == '__main__':
    test_cases = [
        [4, -1, -3, 1, 2, -1],
        [1, 2, 3, 4],
        [0, 0, 0],
        [-3, 1, 2, -3, 4, 0],
        [1, -1, 2, -2, 3, -3] * 5
    ]

    for index, test_case in enumerate(test_cases):
        result = find_zero_sum_subarrays(test_case)
        print(f"Test case {index + 1} returned indices: {result}")

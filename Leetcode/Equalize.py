def minOperations(arr, threshold, d):
    from collections import defaultdict
    
    operation_counts = defaultdict(list)
    
    for num in arr:
        value = num
        operations = 0
        while value > 0:
            operation_counts[value].append(operations)
            value //= d
            operations += 1
        operation_counts[0].append(operations) 
    
    min_operations = float('inf')
    
    for value, ops_list in operation_counts.items():
        if len(ops_list) >= threshold:
            ops_list.sort()
            min_operations = min(min_operations, sum(ops_list[:threshold]))
    
    return min_operations

# Example usage:
arr = [1, 2, 3, 4, 5]
threshold = 3
d = 2
print(minOperations(arr, threshold, d))  # Output: 2

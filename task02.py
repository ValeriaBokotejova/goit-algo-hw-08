import heapq

def merge_k_lists(lists):
    # Min-heap to maintain the smallest elements
    min_heap = []
    
    # Initialize the heap with the first elements of each list
    for i, lst in enumerate(lists):
        if lst:  # If the list is not empty
            heapq.heappush(min_heap, (lst[0], i, 0))  # (value, list index, element index)

    result = []
    
    # While there are elements in the heap
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)
        
        # If there are more elements in the list, add the next one to the heap
        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1], list_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return result

# Example usage
lists = [[2, 4, 5], [1, 5, 6], [1, 3]]
merged_list = merge_k_lists(lists)
print("Merged sorted list:", merged_list)
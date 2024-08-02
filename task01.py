import heapq

def minimize_cable_cost(cables):
    # Create a min-heap from the cable lengths
    heapq.heapify(cables)
    total_cost = 0

    # Continue combining cables until only one is left
    while len(cables) > 1:
        # Remove the two shortest cables
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Combine them
        combined = first + second
        total_cost += combined
        
        # Add the combined cable back to the heap
        heapq.heappush(cables, combined)
    
    return total_cost

# Example usage
cables = [6, 3, 2, 4, 5]
print("Minimum cost to connect the cables:", minimize_cable_cost(cables))
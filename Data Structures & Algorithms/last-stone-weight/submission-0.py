import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Multiply by -1 to simulate a max-heap using Python's min-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        # Continue smashing until 0 or 1 stone remains
        while len(max_heap) > 1:
            # Pop the two heaviest stones (convert back to positive values)
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            
            # If they are not equal, push the difference back into the heap
            if x != y:
                heapq.heappush(max_heap, -(y - x))
                
        # Return the remaining stone's weight or 0 if none remain
        return -max_heap[0] if max_heap else 0

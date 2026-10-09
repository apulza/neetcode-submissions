import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the Min-Heap with the first k largest elements.
        """
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        # Maintain only the k largest elements in the heap
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the current k-th largest element.
        """
        heapq.heappush(self.heap, val)
        
        # If the heap size exceeds k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root of the min-heap is always the k-th largest element
        return self.heap[0]

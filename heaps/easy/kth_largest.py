
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        for i in range(len(nums) - k):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # If i do not have kth greatest elements yet
        if len(self.nums) != self.k:
            heapq.heappush(self.nums, val)
            return self.nums[0]
        if val >= self.nums[0]:
            # Pop and return the smallest item from the heap, 
            # and also push the new item. The heap size doesn’t change
            return heapq.heapreplace(self.nums, val)
        else:
            return self.nums[0]

if __name__ == "__main__":
    obj = KthLargest(2, [0])
    param1 = obj.add(-1)
    param2 = obj.add(1)
    param3 = obj.add(-2)
    param4 = obj.add(-4)
    param5 = obj.add(3)

    print(param1)
    print(param2)
    print(param3)
    print(param4)
    print(param5)
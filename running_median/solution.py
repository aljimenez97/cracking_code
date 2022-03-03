import heapq

def balance_heaps(left_heap, right_heap):
    while abs(len(left_heap) - len(right_heap)) > 1:
        if len(left_heap) > len(right_heap):
            popped = heapq.heappop(left_heap)
            heapq.heappush(right_heap, -popped)
        else:
            popped = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -popped)

def runningMedian(a):
    # Write your code here
    left_heap = []
    right_heap = []
    
    heapq.heapify(left_heap)
    heapq.heapify(right_heap)
    
    medians = []
    
    for number in a:
        if not len(right_heap) or number < right_heap[0]:
            heapq.heappush(left_heap, -number)
        else:
            heapq.heappush(right_heap, number)

        
        balance_heaps(left_heap, right_heap)

        if len(left_heap) == len(right_heap):
            medians.append(float((-left_heap[0] + right_heap[0]) / 2)) 
        elif len(left_heap) > len(right_heap):
            medians.append(float(-left_heap[0]))
        else:
            medians.append(float(right_heap[0]))
    return medians

if __name__ == "__main__":
    input = [1,2,3,4,5,6,7,8,9,10]
    medians = runningMedian(input)
    print(medians)
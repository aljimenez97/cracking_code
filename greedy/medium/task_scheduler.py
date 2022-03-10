# https://leetcode.com/problems/task-scheduler/

# Given a characters array tasks, representing the tasks a CPU needs to do, 
# where each letter represents a different task. Tasks could be done in any order. 
# Each task is done in one unit of time. For each unit of time, the CPU could 
# complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period 
# between two same tasks (the same letter in the array), that is that there must 
# be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all 
# the given tasks.

from collections import Counter, deque
import heapq

def scheduler(tasks, n):
    task_count = Counter(tasks)

    queue = deque()

    max_heap = []
    max_heap.extend([-task_count[i] for i in task_count])
    heapq.heapify(max_heap)

    time = 0

    while max_heap or queue:
        time += 1

        if max_heap:
            task = heapq.heappop(max_heap)
            if task < -1:
                queue.append((task + 1, time + n))

        if queue and queue[0][1] == time:
            popped = queue.popleft()
            heapq.heappush(max_heap, popped[0])

    return time


if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B", "C", "C", "C"]
    n = 2

    print(scheduler(tasks, n))
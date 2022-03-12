# https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 
# 0 to numCourses - 1. You are given an array prerequisites where
# prerequisites[i] = [ai, bi] indicates that you must take course bi first 
# if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have 
# to first take course 1.
# Return the ordering of courses you should take to finish all courses. 
# If there are many valid answers, return any of them. If it is impossible 
# to finish all courses, return an empty array.

from collections import deque

def order_schedule(n_courses, requisites):
        adj_dict = {i: [] for i in range(n_courses)}
        adj_dict_2 = {i: [] for i in range(n_courses)}
        start_candidates = {i for i in range(n_courses)}

        for course, req in requisites:
            adj_dict[course].append(req)
            adj_dict_2[req].append(course)
            if course in start_candidates: start_candidates.remove(course)

        if not start_candidates:
            return []

        q = deque()
        
        for cand in list(start_candidates):
            q.appendleft(cand)

        out = []

        while q:
            popped = q.pop()
            out.append(popped)

            for c in adj_dict_2[popped]:
                adj_dict[c].remove(popped)
                if len(adj_dict[c]) == 0: q.appendleft(c)

        return out if len(out) == n_courses else []

if __name__ == "__main__":
    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]
    
    print(order_schedule(numCourses, prerequisites))
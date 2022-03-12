# https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 
# to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] 
# indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

def schedule(nCourses, requisites):
    my_dict = {i: [] for i in range(nCourses)}

    for course, req in requisites:
        my_dict[course].append(req)
    
    visit = set()

    def dfs(course):
        if course in visit:
            return False
        if my_dict[course] == []:
            return True

        visit.add(course)
        
        for req in my_dict[course]:
            if not dfs(req):
                return False
        
        visit.remove(course)
        my_dict[course] = []

        return True
    
    for i in range(nCourses):
        if not dfs(i):
            return False
    return True
        


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    print(schedule(numCourses, prerequisites))

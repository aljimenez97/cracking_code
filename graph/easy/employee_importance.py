from collections import deque

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

def get_total_importance(employees, employee_id):
    employee_dict = {e.id: e for e in employees}

    q = deque()
    visited = []

    importance = 0
    employee = employee_dict[employee_id]
    q.appendleft(employee)

    while len(q):
        employee = q.pop()
        importance += employee.importance
        visited.append(employee.id)

        for s in employee.subordinates:
            if s not in visited:
                q.appendleft(employee_dict[s])
    return importance



if __name__ == "__main__":
    e1 = Employee(1, 5, [2,3])
    e2 = Employee(2, 3, [])
    e3 = Employee(3, 3, [])

    print(get_total_importance([e1, e2, e3], 1))
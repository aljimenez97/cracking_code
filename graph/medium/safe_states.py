# https://leetcode.com/problems/find-eventual-safe-states/

# There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
# The graph is represented by a 0-indexed 2D integer array graph where graph[i] 
# is an integer array of nodes adjacent to node i, meaning there is an edge from 
# node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node 
# if every possible path starting from that node leads to a terminal node.

# Return an array containing all the safe nodes of the graph. The answer should 
# be sorted in ascending order.

def safe_states(graph):
    adj_dict = {i: [] for i in range(len(graph))}
    terminal_nodes = set()

    for i in range(len(graph)):
        adj_dict[i].extend(graph[i])
        if not len(graph[i]):
            terminal_nodes.add(i)

    visit = set()

    def dfs(node):
        if node in visit:
            return False
        if adj_dict[node] == []:
            return True
        visit.add(node)
        for n in adj_dict[node]:
            if not dfs(n):
                return False
        visit.remove(node)
        adj_dict[node] = []
        return True
    
    out = []
    for i in range(len(graph)):
        if dfs(i):
            out.append(i)
    return out



if __name__ == "__main__":
    graph = [[],[0,2,3,4],[3],[4],[]]
    print(safe_states(graph))


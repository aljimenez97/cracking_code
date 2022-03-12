# https://leetcode.com/problems/reconstruct-itinerary/

# You are given a list of airline tickets where tickets[i] = [fromi, toi] 
# represent the departure and the arrival airports of one flight. 
# Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the 
# itinerary must begin with "JFK". If there are multiple valid itineraries, 
# you should return the itinerary that has the smallest lexical order when 
# read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical 
# order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must 
# use all the tickets once and only once.#

def itineraries(tickets):
    adj = {src: [] for src, _ in tickets}

    tickets.sort()

    for src, dst in tickets:
        adj[src].append(dst)

    res = ["JFK"]

    def dfs(src):
        if len(res) == len(tickets) + 1:
            return True
        if src not in adj:
            return False

        temp = list(adj[src])

        for i, dst in enumerate(temp):
            adj[src].pop(i)
            res.append(dst)
            if dfs(dst):
                return True
            adj[src].insert(i, dst)
            res.pop()
        
        return False

    dfs("JFK")
    return res
            

if __name__ == "__main__":
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(itineraries(tickets))

    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(itineraries(tickets))

    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print(itineraries(tickets))

    tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
    print(itineraries(tickets))

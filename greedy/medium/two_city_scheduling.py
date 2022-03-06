# https://leetcode.com/problems/two-city-scheduling/

# A company is planning to interview 2n people. Given the array costs where 
# costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a 
# is aCosti, and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city such that exactly 
# n people arrive in each city.

def schedule(costs):
    costs_opportunity = [ [c[0], c[1], c[0] - c[1]] for c in costs]
    costs_opportunity.sort(key= lambda x: abs(x[2]), reverse=True)

    total_cost = 0
    total_a = 0
    total_b = 0

    for c in costs_opportunity:
        if (c[2] > 0 and total_b < len(costs) // 2) or total_a == len(costs) // 2:
            total_cost += c[1]
            total_b += 1
        else:
            total_cost += c[0]
            total_a += 1
    return total_cost

if __name__ == "__main__":
    costs = [[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]
    min_cost = schedule(costs)

    print(min_cost)
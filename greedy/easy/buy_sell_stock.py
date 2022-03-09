# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given 
# stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one 
# stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.


def max_profit(prices):
    l = 0
    r = 1
    max_profit = 0


    while r < len(prices):
        if prices[r] - prices[l] > 0:
            max_profit = max( max_profit, prices[r] - prices[l])
        else:
            l = r
        r += 1
    return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(max_profit(prices))
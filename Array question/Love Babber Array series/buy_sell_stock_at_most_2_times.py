'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
'''
'''Approach:
'''

def buySellAtMoset2(ind,buy,prices,cap):
    n = len(prices)
    dp = [[[0]*(cap+1) for _ in range(buy+1)] for _ in range(n+1)]
    for ind in range(n-1,-1,-1):
        for buy in range(0,2):
            for cap in range(1,3):
                if buy==0:
                    do_buy = -prices[ind] + dp[ind + 1][1][cap]
                    not_buy = 0 + dp[ind + 1][0][cap]
                    dp[ind][buy][cap] = max(not_buy,do_buy)
                else:
                    do_sell = prices[ind] + dp[ind + 1][0][cap - 1]
                    not_sell = 0 + dp[ind + 1][1][cap]
                    dp[ind][buy][cap] = max(not_sell,do_sell)
    return dp[0][0][2]

prices = [3,3,5,0,0,3,1,4]
print(buySellAtMoset2(0,1,prices,2))

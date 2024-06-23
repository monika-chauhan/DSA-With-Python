'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

'''Approach:
price   buy/min(buy,price)     sell/max(sell,price-buy)
        inf                         -inf
7       7                            0
1       1                            -6
5       1                             4
3       1                             4
6       1                             5
4       1                             5 = ans        
'''

def max_profit(prices):
    buy = float('inf')
    sell = float('-inf')
    for price in prices:
        buy = min(buy,price)
        sell = max(sell,price-buy)
    
    return sell 

prices = [7,1,5,3,6,4]
print(max_profit(prices))
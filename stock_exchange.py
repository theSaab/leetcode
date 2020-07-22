'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''

price = [7, 1, 7, 3, 6, 4]


def stock(prices):
    profit = 0
    for element in prices[1:]:
        if element < 0:
            continue
        else:
                
            best = prices[0]
            if element < best:
                prices = prices[prices.index(element):]
                stock(prices)
                break
            else:
                if (element - best) > profit:
                    profit = (element - best)
    else:
        print(profit)
stock(price)



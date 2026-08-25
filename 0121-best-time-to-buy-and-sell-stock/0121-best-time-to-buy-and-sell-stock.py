class Solution():
    def maxProfit(self, prices):
        min_price=prices[0]
        max_profit=0
        for price in prices:
            if min_price>price:
                min_price=price
            profit=price-min_price
            if profit>max_profit:
                max_profit=profit
        return max_profit
honey=Solution()
x=honey.maxProfit([7,1,5,3,6,4])
print(x)            
                
      
class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0 
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i] # 낮은 가격이 생기면 사기
            elif prices[i] - buy > profit:
                profit = prices[i] -buy # profit 업데이트는 따른걸루
        return profit
            
        

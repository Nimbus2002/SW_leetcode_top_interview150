class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curhold, curnothold = -float('inf'), 0 # 첫날에는 impossible to sell 그러므로 -무한대로
        for stockprice in prices:
            prevhold , prevnothold = curhold, curnothold
            
            # 가지거나 팔거나 
            curhold = max(prevhold, prevnothold - stockprice) 

            curnothold = max(prevnothold, prevhold + stockprice)

        return curnothold

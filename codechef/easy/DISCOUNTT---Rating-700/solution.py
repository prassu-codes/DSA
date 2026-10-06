class Solution:
    def check_coupon(self, n, x, y, prices):
        originalcost=sum(prices)
        summ=x 
        for i in prices:
            if i>=y:
                summ+=i-y 
        return "COUPON" if summ<originalcost else "NO COUPON"
        # write your code here
        

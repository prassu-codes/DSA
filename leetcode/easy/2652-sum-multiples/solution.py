class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def get_sum(k):
            m=n//k 
            return k*m*(m+1)//2
        return get_sum(3)+get_sum(5)+get_sum(7)-get_sum(15)-get_sum(35)-get_sum(21)+get_sum(105)
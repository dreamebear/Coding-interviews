class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        
        # return x^n
        
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
        
        n = abs(n)
        
        res = 1
        cur = x
        
        while n > 0:
            if n % 2 == 1:
                res *= cur
                
            cur *= cur
            n /= 2
            
        return res

test = Solution()
x = 2.10000
n = 3
print(test.myPow(x, n))
class Solution(object):
    def func(self,num):
        if num==0 or num==1:
            return num
        return self.func(num-1)+self.func(num-2)
    
    def fib(self, n):
        answer= self.func(n)
        return answer
        """
        :type n: int
        :rtype: int
        """
        
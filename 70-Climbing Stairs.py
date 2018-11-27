'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''

# by myself
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = [1, 2, 3]
        if n < 4:
            return fib[n-1]
        for k in range(3, n+1):
            fib[2] = fib[0] + fib[1]              # 永远只存3个元素，save space
            fib[0], fib[1] = fib[1], fib[2]
        return fib[2]

#by others
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        sqrt5 = math.sqrt(5)
        fibn = pow((1 + sqrt5) / 2, n+1) - pow((1 - sqrt5) / 2, n+1)
        return int(float(fibn/sqrt5))

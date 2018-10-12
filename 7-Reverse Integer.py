'''
给定一个 32 位有符号整数，将整数中的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
'''

#by myself
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            a = eval(''.join(reversed(str(x))).strip('0'))
            if a > 2**31-1:
                return 0
            else:
                return a
        elif x < 0:
            b = eval('-'+''.join(reversed(str(abs(x)))).strip('0'))
            if b < -2**31:
                return 0
            else:
                return b
        else:
            return 0

#others
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10
        return res if res <= 0x7fffffff else 0
        
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """    
        x = -int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])   # [:-1]相当于把负号去掉
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x

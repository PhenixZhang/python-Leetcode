'''
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
示例 1:
输入: a = "11", b = "1"
输出: "100"
示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
'''

# by myself
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not eval(a) or not eval(b):
            return str(max(eval(a),eval(b)))
        sum = int(a,2) + int(b,2)
        c = ''
        n = max(len(a),len(b))
        for i in range(n + 1,0,-1):
            if sum // 2**(i-1):
                sum -= 2**(i-1)
                c += '1'
            else:
                c += '0'
        return c.lstrip('0')

# by myself
class Solution:
    def addBinary(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]

# by others
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '' or b == '':
            return a + b
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        elif a[-1] == '1' and b[-1] == '1':
            return self.addBinary(a[:-1], self.addBinary(b[:-1], '1')) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'

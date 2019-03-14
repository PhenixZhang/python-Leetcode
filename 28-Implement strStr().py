'''
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
'''

# by myself
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if needle in haystack:
            return len(haystack.split(needle,1)[0])
        else:
            return -1

# by myself
class Solution:
    def strStr(self, haystack, needle):
        len1 = len(haystack)
        len2 = len(needle)
        if len2 == 0:
            return 0
        if len1 == 0 or len1 < len2:
            return -1
        if len1 == len2:
            if haystack == needle:
                return 0
            else:
                return -1
        for i in range(len1 - len2 + 1):
            if haystack[i:i+len2] == needle:
                return i
        else:
            return -1
        
# by others
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
'''

#by myself
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """      
        a = 0
        if len(strs) == 0:
            return ""
        if len(strs) == 2:
            for j in range(len(min(strs,key=len))):
                if strs[0][j] == strs[1][j]:
                    a += 1
                else:
                    break
            return strs[0][:a]
        for j in range(len(min(strs,key=len))):         
            for i in range(len(strs)-1):
                if strs[i][j] == strs[i+1][j]:
                    continue
                else:
                    break
            else:
                a += 1
        if a == 0:
            return ""
        else:
            return strs[0][:a]

# by others
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]

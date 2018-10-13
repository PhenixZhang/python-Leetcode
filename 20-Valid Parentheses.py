'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
'''

# by myself
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftP = '([{'
        rightP = ')]}'
        stack = []
        for char in s:
            if char in leftP:
                stack.append(char)
            if char in rightP:
                if not stack:
                    return False
                tmp = stack.pop()
                if char == ')' and tmp != '(':
                    return False
                if char == ']' and tmp != '[':
                    return False       
                if char == '}' and tmp != '{':
                    return False
        return stack == []

#by others
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False

        index = 0
        stack = [i for i in s]
        map1 = {"(": ")", "[": "]", "{": "}"}

        while len(stack) > 0:
            # 判断索引是否超过边界
            if index >= len(stack)-1:
                return False
            b = stack[index]
            e = stack[index+1]
            if b not in map1.keys():
                return False
            elif e in map1.keys():
                index += 1
            elif map1[b] == e:
                stack.pop(index+1)
                stack.pop(index)
                index = 0 if index-1<0 else index-1
            else:
                return False
        return stack == []

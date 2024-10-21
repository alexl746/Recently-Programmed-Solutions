#Given a string s, find the length of the longest substring without repeating characters. (Ran in 171 ms)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        wd = []
        ans = 0
        i = 0
        repeat = False
        while i != len(s):
            for n1 in range(len(wd)):
                if wd[n1] == s[i]:
                    repeat = True
                    rep = wd[n1]
            while repeat == True:
                repeat = False
                while wd[0] != rep:
                    wd.pop(0)
                wd.pop(0)
            wd.append(s[i])
            if len(wd) > ans:
                ans = len(wd)
            i += 1
        return ans

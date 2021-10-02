'''
https://leetcode.com/problems/longest-common-prefix/


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example
1:
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Example
2:
Input: strs = ["dog", "racecar", "car"]
Output: ""

Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower - case English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ''

        min_len = min(list(map(len, strs)))

        if min_len == 0:
            return ''

        prefix = ''

        for i in range(min_len):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return prefix
            prefix += char

        return prefix


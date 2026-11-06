class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        current=""
        for char in s:
            if char in current:
                current =current[current.index(char)+1:]
            current+=char
            if len(current)>longest:
                longest=len(current)
        return longest
           
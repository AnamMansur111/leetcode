class Solution:
    def findLHS(self, nums: list[int]) -> int:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        longest = 0

        for num in freq:
            if num + 1 in freq:
                current = freq[num] + freq[num + 1]

                if current > longest:
                    longest = current

        return longest
       
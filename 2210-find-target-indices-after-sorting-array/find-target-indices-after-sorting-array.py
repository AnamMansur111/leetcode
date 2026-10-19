class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        nums.sort()
        k=[]
       
        for i in range(len(nums)):
            if nums[i]==target:
                k.append(i)
        return k

        
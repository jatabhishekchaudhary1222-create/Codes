class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        i=1
        s=nums[0]
        while(i<len(nums)):
            if(nums[i]!=nums[i-1]+1):
                break
            s+=nums[i]
            i+=1
        a=set(nums)
        while s in a:
            s+=1
        return s

                
            
        
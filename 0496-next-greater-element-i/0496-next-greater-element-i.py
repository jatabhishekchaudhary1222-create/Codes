class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        d={}
        for i in reversed(nums2):
            while stack and stack[-1]<=i:
                stack.pop()
            if stack:
                d[i]=stack[-1]
            else:
                d[i]=-1
            stack.append(i)
        return [d[c] for c in nums1]
        
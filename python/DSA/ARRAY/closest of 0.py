nums=[-4,-2,8,2,1,3]
class Solution:
    def findClosestNumber(self, nums:list[int]) -> int:
        closest=nums[0]#init set the num
        for i in range(1,len(nums)):
            current=nums[i]
            if abs(nums[i])<abs(closest):
                closest=i
         
        if closest==current and abs(closest) in nums:
            return abs(closest)
        else:
            return closest      
print(Solution().findClosestNumber(nums))

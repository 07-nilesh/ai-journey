class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return[i,j]
        return []
solver=Solution()
nums =[24,53,5,2]
target_input=int(input("enter target : "))
result=solver.twoSum(nums,target_input)

if result:
    print(f"Indices found : {result}")
else:
    print("No pair found")
        
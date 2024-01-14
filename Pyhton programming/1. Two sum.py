nums = [2,7,11,15]
target=int(input())

def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
           if nums[i]+nums[j]==target:
               return [i,j]
print(twoSum(nums,target))
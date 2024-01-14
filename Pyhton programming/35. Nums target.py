def searchInsert(nums: list, target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums=sorted(list(nums))
        return nums.index(target)
    
lst=list(map(int,input("Enter nums sep space: ").split()))
target=int(input("Enter target: "))
print(searchInsert(lst,target))
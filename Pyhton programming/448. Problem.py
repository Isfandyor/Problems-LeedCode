def findDisappearedNumbers(nums: list) ->list:
         return set(range(1, len(nums)+1)).difference(set(nums))
print(findDisappearedNumbers([1,2,3,4,7,8]))








       
import itertools

n = int(input("Enter n: "))
k = int(input("Enter k: ")) - 1

nums = list(range(1, n + 1))
permutations = list(itertools.permutations(nums))
result = "".join(map(str, permutations[k]))

print(result)




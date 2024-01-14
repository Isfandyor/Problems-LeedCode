class Solution:
    def fizzBuzz(self, n: int) -> list:
        nums=list(range(1,n+1))
        return list(map(lambda son: "FizzBuzz" if son%3==0 and son%5==0 else "Fizz" if son%3==0 else "Buzz" if son%5==0 else str(son),nums))

natija = Solution()

result = natija.fizzBuzz(int(input("Enter size list: ")))
print(result)
# print(natija.fizzBuzz(int(input("Enter size list: "))))
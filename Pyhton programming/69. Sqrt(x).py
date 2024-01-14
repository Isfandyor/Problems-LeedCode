x=int(input())

def mySqrt(x,i=0):
     while (i+1)*(i+1)<=x:
          i+=1   
     return i 
     
print(mySqrt(x))


"The best way is to use the formula:"
# def mySqrt(x: int) -> int:
#         #return int(x**0.5) ---> method 1

#         #method-2
#         if x==0 or x==1:
#             return x
#         guess=x//2
#         while guess*guess>x:
#             guess = (guess + x // guess) // 2
#         return guess

        
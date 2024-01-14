def largestGoodInteger(num: str) -> str:
     st=['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']
     lst=[]
     for i in st:
         if i in num:
             lst.append(i)
     try:
         return lst[0]
     except IndexError:
         return ""
     
"""The best way is this:: 

# def largestGoodInteger(num: str) -> str:
#         for digit in range(9, -1, -1):
#             if str(digit)*3 in num:
#                 return str(digit)*3
        
#         return "" 
# """

num="12351996533377716511666"

print(largestGoodInteger(num))

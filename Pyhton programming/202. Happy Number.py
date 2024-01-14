def HappyNumber(n: int) -> bool:
     st=[]
     while n!=1:
         n=sum(int(i)*int(i) for i in str(n))
         if not n in st:
             st.append(n)
         else:
             return False
     return True    
print(HappyNumber(int(input())))

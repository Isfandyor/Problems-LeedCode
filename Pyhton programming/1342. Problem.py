num=int(input("Enter number: "))

def to_zero(num: int)->int:
    step=0
    while num!=0:
        if num%2:
            k=num
            num-=1
            step+=1
            print(f"Step {step}) {k} is odd; subtract 1 and obtain {num}.")
        else:
            k=num
            num//=2
            step+=1
            print(f"Step {step}) {k} is even; divide by 2 and obtain {num}.")
    return step

print(f"Result is  --> {to_zero(num)}")
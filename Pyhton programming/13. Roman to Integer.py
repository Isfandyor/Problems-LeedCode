def romanToInt(s: str) -> int:
        dct={
            "I" :1,
            "V" :5,
            "X" :10,
            "L" :50,
            "C" :100,
            "D" :500,
            "M" :1000,
        }
        result=0
        for i in range(len(s)-1):
                if dct[s[i]]<dct[s[i+1]]:
                    result-=dct[s[i]]
                else:
                    result+=dct[s[i]]
        return result+dct[s[-1]]
    
roman=input().upper()
print(romanToInt(roman))

# MCMXCIV -> 1000-100+1000-10+100-1+5=1994
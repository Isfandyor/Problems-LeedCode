def halvesAreAlike(s: str) -> bool:
        k=len(s)//2
        s=s.lower()
        alpha='aeiou'
        return sum(1 for i in s[:k] if i in alpha)==sum(1 for i in s[k:] if i in alpha)
        
print(halvesAreAlike(input()))

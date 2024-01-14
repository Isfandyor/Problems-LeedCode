def isPalindrome(s: str) -> bool:
    s=s.lower()
    s=list(filter(lambda a: a.isalnum(),s))
    s_reverse=s[::-1]
    return s==s_reverse
print(isPalindrome("0P"))
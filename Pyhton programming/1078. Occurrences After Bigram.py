# text = "alice is a good girl she is a good student"
# first = "a" 
# second = "good"

text ="jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa"
first ="kcyxdfnoa"
second ="jkypmsxd"
text=text.split()
result=[]
for i in range(len(text)-2):
        if text[i]==first and text[i+1]==second:
            result.append(text[i+2])
print(result)
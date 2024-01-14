def frequencySort(s: str) -> str:
        st=""
        lst=[]
        for i in s:
            if not i in st:
                st+=i  
                lst.append(i*s.count(i)) 
        lst=sorted(lst,key=lambda a: len(a),reverse=True)
        return "".join(lst)
    
print(frequencySort(input()))
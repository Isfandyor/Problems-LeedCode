strs = ["flower","flow","flight"]
def prefix(strs):
    if not strs:
        return "" 
    shrtelem=min(strs,key=len)
    result=""
    
    for i in range(len(shrtelem)):
        char=shrtelem[i]
        if all(j[i]==char for j in strs):
            result+=char
        else:
            break
    return result
    
print(prefix(strs))